"""Rollout step: claim → prepare → run → validate → push.

Differs from ``instantiate_cycle.py`` by design:

- Two stages: ``cfg.stages`` has length 2 — [rollout_stage1,
  rollout_stage2]. Stage 1 edits forge's rendered default system prompt;
  stage 2 runs the rollout with FORGE_SYSTEM_PROMPT_FILE pointing at
  stage 1's output.
- Hard byte-equality gate in ``validate_rollout``: SHA256 of stage 1's
  ``system_prompt.md`` must match the first system message in stage 2's
  ``trace.jsonl`` context event.
- Mutable ``RolloutTask`` dataclass; ``cfg`` is NOT a field — passed as
  the first positional arg everywhere.
- All-exception observability: the per-attempt closure catches
  ``Exception`` and appends a full record to ``cfg.failure_log_path``
  before re-raising so ``retry_with`` sees the failure.
- Wipe-and-redo retry: every attempt wipes ``task.work_dir`` and
  recreates from scratch. No ``.source_pulled`` / per-stage ``.done`` /
  ``.pushed`` markers.
- Local-only preflight is just ``_check_uv_cache_dir``: other problems
  surface in the failure log on the first task.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import logging
import random
import shlex
import shutil
import time
from dataclasses import dataclass
from importlib.resources import files
from pathlib import Path

import httpx
from pydantic import BaseModel
from tenacity import RetryError, stop_after_attempt

from office_files_pipeline.config import RolloutConfig, StepConfig
from office_files_pipeline.expand import expand_cmd
from office_files_pipeline.failures import CommandError, ValidationError, dump_failure
from office_files_pipeline.remote import claim_once, run_rsync
from office_files_pipeline.retry import retry_with

log = logging.getLogger("ofpipe.rollout")

# ── Module constants ────────────────────────────────────────────────────

# AGENTS.md and draw.py ship inside the package; each task gets fresh
# copies from the installed package (importlib.resources).
ROLLOUT_STATIC_DIR = Path(str(files("office_files_pipeline").joinpath("rollout_static")))
EXCLUDED_DIRNAMES = {"node_modules", ".venv", "__pycache__", ".cache", ".done"}


# ── Types ───────────────────────────────────────────────────────────────


class RolloutClaimItem(BaseModel):
    """Claim payload from ``POST /claim/rollout``."""

    instantiate_hash: str


@dataclass
class RolloutTask:
    """Per-claim runtime state. Mutable. ``cfg`` is NOT a field — passed
    as the first positional arg everywhere.
    """

    instantiate_hash: str
    work_dir: Path
    start_ts: float = 0.0
    attempt_count: int = 0
    stage1_skipped: bool = False  # single source of truth for the arm

    @property
    def task_hash(self) -> str:
        """Alias for instantiate_hash, used by failures.dump_failure."""
        return self.instantiate_hash


def _should_skip_stage1(task_hash: str, prob: float) -> bool:
    """Deterministic per-task: same task hash always makes the same decision.

    Maps the first 32 bits of the task hash (hex) to [0, 1) and compares
    to ``prob``. Reproducibility: given the task hashes and prob, you can
    predict which tasks were in the baseline-passthrough arm without
    scanning artifacts.
    """
    if prob <= 0.0:
        return False
    bucket = int(task_hash[:8], 16) / (1 << 32)
    return bucket < prob


@dataclass(frozen=True)
class RolloutExpansionContext:
    """Placeholder values for the rollout ``cmd`` templates.

    Distinct from instantiate's ``ExpansionContext`` because the rollout
    templates use a different placeholder set (no ``{stage_dir}``).
    ``expand_cmd`` is duck-typed on ``ctx.as_dict()``.
    """

    work_dir: Path
    output_dir: Path
    prompt: str

    def as_dict(self) -> dict[str, str]:
        return {
            "work_dir": shlex.quote(str(self.work_dir)),
            "output_dir": shlex.quote(str(self.output_dir)),
            "prompt": shlex.quote(self.prompt),
        }


# ── build_rollout_task ──────────────────────────────────────────────────


def build_rollout_task(cfg: RolloutConfig, claim: RolloutClaimItem) -> RolloutTask:
    """Pure-python builder; safe outside any retry boundary."""
    return RolloutTask(
        instantiate_hash=claim.instantiate_hash,
        work_dir=cfg.output_dir / f"task_{claim.instantiate_hash}",
    )


# ── prepare_rollout ─────────────────────────────────────────────────────


async def prepare_rollout(cfg: RolloutConfig, task: RolloutTask) -> None:
    """Pull prompt + reference_files from the artifact tree; create dirs; copy
    AGENTS.md; copy modify-agent prompt; render baseline system prompt.

    Layout:
    - ``task.work_dir/rollout_stage1_prompt.md``    (modify-agent's user prompt)
    - ``task.work_dir/rollout_stage2_prompt.md``    (renamed from prompt.md; AGENTS.md hint appended)
    - ``task.work_dir/work/AGENTS.md``              (forge auto-injects into system prompt)
    - ``task.work_dir/work/reference_files/``       (chmod 555 nudge)
    - ``task.work_dir/work/deliveries/``            (pre-created, chmod 755)
    - ``task.work_dir/trace/``                      (cowbox --rw for FORGE_TRACE_FILE)
    - ``task.work_dir/prompt_customize/``           (stage 1's flat workdir)
    - ``task.work_dir/prompt_customize/system_prompt_original.md`` (rendered baseline)

    Order matters: ``work/`` must be fully populated (AGENTS.md copied,
    reference_files chmod'd) BEFORE ``render_system_prompt`` runs — the rendered
    output reflects ``git ls-files`` and ``list_current_directory()`` against
    ``work/``. Stage 2 runs against the SAME ``work/`` state.
    """
    shard = task.instantiate_hash[:3]
    work = task.work_dir / "work"
    trace = task.work_dir / "trace"
    pc = task.work_dir / "prompt_customize"

    work.mkdir(parents=True)
    (work / "deliveries").mkdir()
    (work / "deliveries").chmod(0o755)
    trace.mkdir()
    pc.mkdir()

    # Copy draw.py into stage1's flat workdir — the modify agent uses it
    # to commit to a posture drawn uniformly from a support it constructs.
    shutil.copy(ROLLOUT_STATIC_DIR / "draw.py", pc / "draw.py")

    # rsync the user prompt directly to its stage-2 name
    src_root = (
        f"rsync://{cfg.client.rsync_host}:{cfg.client.rsync_port}/"
        f"artifacts/office-files-instantiate/{shard}/"
        f"task_{task.instantiate_hash}/stage2/"
    )
    await run_rsync(
        ["-az", src_root + "prompt.md", str(task.work_dir / "rollout_stage2_prompt.md")],
        name=f"pull prompt task_{task.instantiate_hash}",
    )

    # Append the AGENTS.md hint
    p = task.work_dir / "rollout_stage2_prompt.md"
    p.write_text(
        p.read_text(encoding="utf-8")
        + "\n\n**IMPORTANT**: Operational guidelines in AGENTS.md",
        encoding="utf-8",
    )

    # rsync reference files, then make them read-only
    await run_rsync(
        [
            "-az",
            "--mkpath",
            src_root + "reference_files/",
            str(work / "reference_files/"),
        ],
        name=f"pull refs task_{task.instantiate_hash}",
    )
    refs = work / "reference_files"
    for q in refs.rglob("*"):
        q.chmod(0o555 if q.is_dir() else 0o444)
    refs.chmod(0o555)

    # AGENTS.md from package install
    shutil.copy(ROLLOUT_STATIC_DIR / "AGENTS.md", work / "AGENTS.md")

    # Copy modify-agent prompt from package install
    meta_prompt_src = Path(
        str(files("office_files_pipeline").joinpath("prompts/rollout_prompt_customize.md"))
    )
    shutil.copy(meta_prompt_src, task.work_dir / "rollout_stage1_prompt.md")

    # Render baseline system prompt — work/ must be fully populated by here
    await render_system_prompt(cfg, task)


# ── render_system_prompt ───────────────────────────────────────────────


async def render_system_prompt(cfg: RolloutConfig, task: RolloutTask) -> None:
    """Run the prepare-time render subprocess; capture stdout to
    ``prompt_customize/system_prompt_original.md``.

    ``forge prompt render`` is deterministic (no LLM call) and depends on cwd
    state — ``work/`` must be fully populated by the caller before this runs.
    The ``render_cmd`` template carries the FORGE_SESSION__* env shell prefix.
    """
    ctx = RolloutExpansionContext(
        work_dir=task.work_dir.resolve(),
        output_dir=cfg.output_dir.resolve(),
        prompt="",  # unused by render_cmd; satisfies the dataclass
    )
    argv = expand_cmd(cfg.render_cmd, ctx)
    out_path = task.work_dir / "prompt_customize" / "system_prompt_original.md"

    # Open the output file BEFORE creating the subprocess so a failure to open
    # surfaces synchronously rather than as a confusing pipe-closed error.
    with out_path.open("wb") as fh:
        proc = await asyncio.create_subprocess_exec(
            *argv,
            stdin=asyncio.subprocess.DEVNULL,  # defensive: forge must never wait on stdin
            stdout=fh,
            stderr=asyncio.subprocess.PIPE,
        )
        _, stderr_b = await proc.communicate()

    if proc.returncode != 0:
        raise CommandError(
            f"render (task_{task.instantiate_hash}): forge prompt render exit {proc.returncode}",
            stdout="",  # we routed stdout to file
            stderr=stderr_b.decode(errors="replace"),
            returncode=proc.returncode,
        )

    if out_path.stat().st_size == 0:
        raise CommandError(
            f"render (task_{task.instantiate_hash}): system_prompt_original.md is empty after render",
            stdout="", stderr="", returncode=0,
        )


# ── run_stage ───────────────────────────────────────────────────────────


async def run_stage(cfg: RolloutConfig, task: RolloutTask, stage: StepConfig) -> None:
    """Invoke cowbox+forge for one stage. Raises ``CommandError`` on non-zero
    exit with full streams.

    Stage 1 reads ``rollout_stage1_prompt.md``, stage 2 reads
    ``rollout_stage2_prompt.md``. The prompt-file index matches
    ``cfg.stages.index(stage) + 1``.
    """
    stage_index = cfg.stages.index(stage) + 1  # 1-based for filename
    prompt_path = task.work_dir / f"rollout_stage{stage_index}_prompt.md"
    prompt_text = prompt_path.read_text(encoding="utf-8")

    ctx = RolloutExpansionContext(
        work_dir=task.work_dir.resolve(),
        output_dir=cfg.output_dir.resolve(),
        prompt=prompt_text,
    )
    argv = expand_cmd(stage.cmd, ctx)

    proc = await asyncio.create_subprocess_exec(
        *argv,
        stdin=asyncio.subprocess.DEVNULL,  # defensive: forge must never wait on stdin
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    try:
        out_b, err_b = await asyncio.wait_for(proc.communicate(), timeout=stage.timeout)
    except TimeoutError:
        proc.kill()
        await proc.wait()
        raise

    if proc.returncode != 0:
        raise CommandError(
            f"{stage.name} (task_{task.instantiate_hash}): forge exit {proc.returncode}",
            stdout=out_b.decode(errors="replace"),
            stderr=err_b.decode(errors="replace"),
            returncode=proc.returncode,
        )


# ── validate_stage1 ───────────────────────────────────────────────────


def validate_stage1_basic(cfg: RolloutConfig, task: RolloutTask) -> None:
    """Always-applicable stage1 done-gates: ``system_prompt.md`` exists
    and is non-empty; ``.done`` present.

    An empty system prompt makes stage 2's model request fail with an
    HTTP 400; detect it here so the failure surfaces with a clear
    "stage1 system_prompt.md is empty" message instead.

    ``cfg`` is unused but kept positional for uniformity with rollout's
    ``(cfg, task)`` convention.
    """
    pc = task.work_dir / "prompt_customize"
    sp = pc / "system_prompt.md"
    if not sp.is_file():
        raise ValidationError(
            f"task {task.instantiate_hash}: stage1 system_prompt.md missing"
        )
    if sp.stat().st_size == 0:
        raise ValidationError(
            f"task {task.instantiate_hash}: stage1 system_prompt.md is empty"
        )
    if not (pc / ".done").exists():
        raise ValidationError(
            f"task {task.instantiate_hash}: stage1 .done missing"
        )


def validate_stage1_tool_use(cfg: RolloutConfig, task: RolloutTask) -> None:
    """Modify-arm-only stage1 gates: ``postures.json`` and ``posture.txt``
    must exist.

    These files are produced by the agent (postures.json) and by draw.py
    (posture.txt). Their absence indicates the agent skipped the
    tool-mediated posture commitment, which would silently bypass the
    diversity mechanism — fail loudly so wipe-and-restart re-rolls.

    ``cfg`` is unused but kept positional for uniformity.
    """
    pc = task.work_dir / "prompt_customize"
    if not (pc / "postures.json").is_file():
        raise ValidationError(
            f"task {task.instantiate_hash}: stage1 postures.json missing — "
            f"agent must construct support and run draw.py"
        )
    if not (pc / "posture.txt").is_file():
        raise ValidationError(
            f"task {task.instantiate_hash}: stage1 posture.txt missing — "
            f"agent must run draw.py against postures.json"
        )


# ── validate_rollout ────────────────────────────────────────────────────


def validate_rollout(cfg: RolloutConfig, task: RolloutTask) -> None:
    """Stage-2 done-gates + byte-equality:

    1. ``work/.done`` (or ``work/deliveries/.done``) exists.
    2. ``work/deliveries/`` has at least one non-excluded file at any depth.
    3. SHA256(``prompt_customize/system_prompt.md``) ==
       SHA256(first system message in ``trace/trace.jsonl``'s context event).
    """
    work = task.work_dir / "work"

    if not (work / ".done").exists() and not (work / "deliveries" / ".done").exists():
        raise ValidationError(
            f"task {task.instantiate_hash}: ./.done missing at workspace root"
        )

    deliveries = work / "deliveries"
    has_content = any(
        p.is_file() and not any(seg in EXCLUDED_DIRNAMES for seg in p.parts)
        for p in deliveries.rglob("*")
    )
    if not has_content:
        raise ValidationError(
            f"task {task.instantiate_hash}: ./deliveries/ empty after exclusions"
        )

    _validate_byte_equality(task)


def _validate_byte_equality(task: RolloutTask) -> None:
    """Hard gate: the system prompt forge sent must be ``system_prompt.md``.

    Reads the ``context`` event that the pinned forge build writes to
    FORGE_TRACE_FILE on the first turn (see docs/operations.md). Failure
    mode meanings:
    - ``trace.jsonl missing`` / ``context event missing``: stage 2's forge
      crashed before writing the trace, OR FORGE_TRACE_FILE wasn't set, OR
      the trace file is corrupt, OR the forge build writes a different
      trace format.
    - ``wire system count != 1``: forge's MergeSystemMessages no longer
      merges system messages for OpenAI-compatible providers, OR the
      FORGE_SYSTEM_PROMPT_FILE override didn't activate.
    - ``byte-equality broken``: either the override didn't reach the wire,
      OR MergeSystemMessages altered a single system message, OR
      ``system_prompt.md`` was modified between validation and stage 2's
      forge invocation (race / pipeline bug).
    """
    sp_path = task.work_dir / "prompt_customize" / "system_prompt.md"
    trace_path = task.work_dir / "trace" / "trace.jsonl"

    if not trace_path.is_file():
        raise ValidationError(
            f"task {task.instantiate_hash}: trace.jsonl missing"
        )

    file_bytes = sp_path.read_bytes()
    file_h = hashlib.sha256(file_bytes).hexdigest()

    wire_content = None
    for line in trace_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        ev = json.loads(line)
        if ev.get("event") == "context":
            sys_msgs = [m["content"] for m in ev["messages"] if m["role"] == "system"]
            if len(sys_msgs) != 1:
                raise ValidationError(
                    f"task {task.instantiate_hash}: wire has {len(sys_msgs)} "
                    f"system messages, expected 1 (forge did not merge them "
                    f"into one; check the forge build)"
                )
            wire_content = sys_msgs[0]
            break

    if wire_content is None:
        raise ValidationError(
            f"task {task.instantiate_hash}: trace.jsonl has no context event"
        )

    wire_h = hashlib.sha256(wire_content.encode("utf-8")).hexdigest()
    if file_h != wire_h:
        raise ValidationError(
            f"task {task.instantiate_hash}: byte-equality broken — "
            f"system_prompt.md SHA256={file_h[:16]} != "
            f"wire system msg SHA256={wire_h[:16]} "
            f"(file_size={sp_path.stat().st_size} bytes, "
            f"wire_size={len(wire_content.encode('utf-8'))} bytes)"
        )


# ── push_rollout ────────────────────────────────────────────────────────


async def push_rollout(cfg: RolloutConfig, task: RolloutTask) -> None:
    """Merge back to the artifact tree: trace.jsonl → deliveries/ →
    system_prompt.md → postures (modify arm only) → rollout.json → .done.

    Push order matters: the ``.done`` marker is the contract downstream
    consumers check; pushing it last guarantees siblings are present
    when ``.done`` appears.
    """
    shard = task.instantiate_hash[:3]
    dst = (
        f"rsync://{cfg.client.rsync_host}:{cfg.client.rsync_port}/"
        f"artifacts/office-files-rollout/{shard}/task_{task.instantiate_hash}/"
    )

    # Write rollout.json with final timing before pushing it
    rollout_json = task.work_dir / "rollout.json"
    rollout_json.write_text(
        json.dumps(
            {
                "start_ts": task.start_ts,
                "elapsed_s": time.time() - task.start_ts,
                "attempt_count": task.attempt_count,
                "stage1_skipped": task.stage1_skipped,
            },
            indent=2,
        )
    )

    await run_rsync(
        [
            "-az",
            "--mkpath",
            str(task.work_dir / "trace" / "trace.jsonl"),
            dst + "trace.jsonl",
        ],
        name=f"push trace task_{task.instantiate_hash}",
    )
    await run_rsync(
        [
            "-az",
            "--mkpath",
            "--exclude=node_modules/",
            "--exclude=.venv/",
            "--exclude=__pycache__/",
            "--exclude=.cache/",
            "--max-size=100M",
            f"{task.work_dir / 'work' / 'deliveries'}/",  # trailing "/": copy the contents
            dst + "deliveries/",
        ],
        name=f"push deliveries task_{task.instantiate_hash}",
    )
    # Per-task customized system prompt — pushed before rollout.json so
    # any consumer that gates on rollout.json sees system_prompt.md too.
    await run_rsync(
        [
            "-az",
            str(task.work_dir / "prompt_customize" / "system_prompt.md"),
            dst + "system_prompt.md",
        ],
        name=f"push system_prompt task_{task.instantiate_hash}",
    )
    # Stage1 modify-arm artifacts — pushed only when stage1 ran.
    # Single-source-of-truth: task.stage1_skipped decides everything
    # (validation, push, rollout.json field).
    if not task.stage1_skipped:
        pc = task.work_dir / "prompt_customize"
        await run_rsync(
            ["-az", str(pc / "postures.json"), dst + "postures.json"],
            name=f"push postures task_{task.instantiate_hash}",
        )
        await run_rsync(
            ["-az", str(pc / "posture.txt"), dst + "posture.txt"],
            name=f"push drawn posture task_{task.instantiate_hash}",
        )
    await run_rsync(
        ["-az", str(rollout_json), dst + "rollout.json"],
        name=f"push rollout.json task_{task.instantiate_hash}",
    )

    # .done LAST — downstream consumers rely on .done implying siblings are present
    marker = task.work_dir / ".done_local"
    marker.touch()
    await run_rsync(
        ["-az", str(marker), dst + ".done"],
        name=f"push .done task_{task.instantiate_hash}",
    )


# ── attempt_rollout ─────────────────────────────────────────────────────


async def attempt_rollout(cfg: RolloutConfig, task: RolloutTask) -> None:
    """One full attempt: wipe → prepare → (stage1 or passthrough) →
    validate_stage1 → stage2 → validate_rollout → push → cleanup.

    Two arms:

    - **Modify arm:** stage 1 runs; ``validate_stage1_basic`` and
      ``_tool_use`` both gate.
    - **Baseline arm** (probability ``cfg.skip_stage1_prob``, deterministic
      per task hash): stage 1 is skipped; ``system_prompt.md`` is a
      byte-copy of ``system_prompt_original.md``; only ``_basic`` gates.
      The byte-equality contract in ``validate_rollout`` still applies —
      the no-modify path of forge's prompt-injection machinery gets
      exercised.

    No try/except — exceptions bubble to ``process_one_rollout``'s retry
    boundary, which dumps to JSONL and triggers the next attempt.
    Wipe-and-restart: stage 1's output is stochastic (in the modify arm),
    so caching it would lock in bad outputs.
    """
    if task.work_dir.exists():
        shutil.rmtree(task.work_dir)
    await prepare_rollout(cfg, task)

    if _should_skip_stage1(task.instantiate_hash, cfg.skip_stage1_prob):
        # Baseline-arm passthrough.
        task.stage1_skipped = True
        pc = task.work_dir / "prompt_customize"
        shutil.copy(pc / "system_prompt_original.md", pc / "system_prompt.md")
        (pc / ".done").touch()
        validate_stage1_basic(cfg, task)
    else:
        # Modify arm — stage 1.
        await run_stage(cfg, task, cfg.stages[0])
        validate_stage1_basic(cfg, task)
        validate_stage1_tool_use(cfg, task)

    # Stage 2 — rollout
    await run_stage(cfg, task, cfg.stages[1])
    validate_rollout(cfg, task)

    await push_rollout(cfg, task)
    shutil.rmtree(task.work_dir)


# ── process_one_rollout ─────────────────────────────────────────────────


async def process_one_rollout(cfg: RolloutConfig, task: RolloutTask) -> None:
    """Per-task retry loop using ``retry_with``. All exceptions → JSONL ledger.

    Uses ``retry_with`` (not a for loop) so rollout inherits the
    ``wait_random(1, 180)`` backoff between attempts. ``retryable=(Exception,)``
    catches everything; explicit for self-documenting code. The inner closure
    handles per-attempt bookkeeping and dumping; ``attempt_rollout`` stays
    pure happy-path.
    """

    async def _attempt() -> None:
        task.attempt_count += 1
        task.start_ts = time.time()
        try:
            await attempt_rollout(cfg, task)
        except Exception as exc:
            dump_failure(cfg, task, exc)
            raise

    try:
        await retry_with(
            _attempt,
            stop=stop_after_attempt(cfg.max_retries),
            retryable=(Exception,),
            name=f"task {task.instantiate_hash}",
        )
        log.info(
            "task %s succeeded in attempt %d (elapsed %.1fs)",
            task.instantiate_hash,
            task.attempt_count,
            time.time() - task.start_ts,
        )
    except RetryError:
        log.error(
            "task %s exhausted %d attempts",
            task.instantiate_hash,
            cfg.max_retries,
        )


# ── worker_cycle_rollout ────────────────────────────────────────────────


async def worker_cycle_rollout(
    cfg: RolloutConfig, http: httpx.AsyncClient
) -> None:
    """Per-coroutine forever-loop. Spawned ``cfg.concurrency`` times by
    ``run_rollout``.

    Claim is in its own try/catch — the coordinator may be restarting
    autossh tunnels and that's not the worker's concern. Empty queues
    sleep-and-continue. Per-task failures are owned by
    ``process_one_rollout`` (which dumps to JSONL and never propagates).
    """
    while True:
        try:
            claim = await claim_once(http, cfg.client, "rollout", RolloutClaimItem)
        except Exception as e:
            log.warning("claim error: %r; backing off", e)
            await asyncio.sleep(random.uniform(1, 60))
            continue

        if claim is None:
            await asyncio.sleep(random.uniform(1, 60))
            continue

        # claim_once's signature returns BaseModel; narrow for the type-checker
        assert isinstance(claim, RolloutClaimItem)
        task = build_rollout_task(cfg, claim)
        log.info("task %s claimed", task.instantiate_hash)
        await process_one_rollout(cfg, task)


# ── preflight_rollout ───────────────────────────────────────────────────


def preflight_rollout(cfg: RolloutConfig) -> None:
    """Local-only preflight: only the cache-dir creation. Other problems
    surface as CommandErrors / ValidationErrors in the failure log on the
    first task. The cache dir is created because cowbox's --rw of a
    non-existent path can be silently odd; mkdir is cheap insurance.
    """
    _check_uv_cache_dir()


def _check_uv_cache_dir() -> None:
    cache = Path("/root/.cache/uv")
    cache.mkdir(parents=True, exist_ok=True)
    if not cache.is_dir():
        raise RuntimeError("rollout preflight: /root/.cache/uv is not a directory")


# ── run_rollout entry ───────────────────────────────────────────────────


async def run_rollout(cfg: RolloutConfig) -> None:
    """Top-level rollout entry. Preflight, wipe ``output_dir``, spawn
    workers, gather forever.

    Mirrors ``instantiate_cycle.run_instantiate``. The startup wipe guards
    against a stale ``output_dir`` from a previous launch leaking into a
    fresh one.
    """
    preflight_rollout(cfg)
    shutil.rmtree(cfg.output_dir, ignore_errors=True)
    cfg.output_dir.mkdir(parents=True)

    async with httpx.AsyncClient() as http:
        workers = [
            asyncio.create_task(worker_cycle_rollout(cfg, http))
            for _ in range(cfg.concurrency)
        ]
        await asyncio.gather(*workers, return_exceptions=True)
    log.info("rollout pipeline complete")
