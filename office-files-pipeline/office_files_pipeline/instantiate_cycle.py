"""Instantiate-step worker cycle: stage 1 (design space + brief), stage 2
(task package), then one push of the assembled output.

Conventions shared with ``rollout_cycle.py``:

- ``cfg`` flows positionally — every helper takes ``(cfg, task, ...)``;
  ``InstantiateTask`` does not carry ``cfg`` as a field.
- Single top-level retry boundary in ``process_one_instantiate``;
  ``retryable=(Exception,)`` catches everything.
- Subprocess non-zero exit raises ``CommandError`` with full untruncated
  ``stdout`` / ``stderr`` / ``returncode``.
- Output-gate failures raise ``ValidationError``; per-stage
  ``shutil.rmtree`` on validation fail — ``.done`` is a
  skip-prepare-and-run gate, never a skip-validation gate.
- ``stage_final_and_push`` always rebuilds ``_final/``.
- Failures dump to ``cfg.failure_log_path`` via the shared
  ``failures.dump_failure``.
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import logging
import random
import shutil
import sys
import time
from dataclasses import dataclass
from importlib.resources import files
from pathlib import Path

import httpx
from pydantic import BaseModel
from tenacity import RetryError, stop_after_attempt

from office_files_pipeline.config import InstantiateConfig, StepConfig
from office_files_pipeline.expand import ExpansionContext, expand_cmd
from office_files_pipeline.failures import CommandError, ValidationError, dump_failure
from office_files_pipeline.remote import claim_once, run_rsync
from office_files_pipeline.retry import retry_with

log = logging.getLogger("ofpipe.instantiate")


# ── Constants (importlib.resources paths) ──────────────────────────────

# Templates and static anchors ship inside the office_files_pipeline wheel.
# VENV_LINK_TARGET is the venv that runs this code — on a worker, the
# workspace venv that ``uv sync`` creates in the repository checkout.
_PACKAGE_ROOT = Path(str(files("office_files_pipeline")))
TEMPLATES_DIR = _PACKAGE_ROOT / "metatemplates" / "task_types"
STATIC_DIR = _PACKAGE_ROOT / "instantiate_static"
# sys.prefix gives the venv root WITHOUT resolving symlinks.
# ``Path(sys.executable).resolve().parent.parent`` would follow the symlink
# in uv-managed venvs into uv's managed CPython install at
# ~/.local/share/uv/python/<...> — the wrong target.
VENV_LINK_TARGET = Path(sys.prefix)

# Stage anchor files (the manifold each stage reads).
STAGE_ANCHORS: dict[str, str] = {
    "stage1": "THE_REAL_WORK_MANIFOLD.md",
    "stage2": "THE_ARTIFACT_SHAPE_MANIFOLD.md",
}

# Required stage-2 output files.
STAGE2_REQUIRED_FILES: tuple[str, ...] = (
    "prompt.md",
    "rubric.md",
    "deliverable_shape.md",
)


# ── Types ──────────────────────────────────────────────────────────────


class InstantiateClaimItem(BaseModel):
    """Claim payload from ``POST /claim/instantiate``."""

    template_id: str
    classify_task_hash: str
    instantiate_hash: str


@dataclass
class InstantiateTask:
    """Per-claim runtime state. Mutable to track ``attempt_count``/``start_ts``.
    No ``cfg`` field — passed positionally everywhere.
    """

    instantiate_hash: str
    classify_task_hash: str
    template_id: str
    work_dir: Path
    stage_dirs: dict[str, Path]
    start_ts: float = 0.0
    attempt_count: int = 0

    @property
    def task_hash(self) -> str:
        """Alias for instantiate_hash, used by failures.dump_failure
        and any other step-agnostic consumer."""
        return self.instantiate_hash


# ── Builders ───────────────────────────────────────────────────────────


def build_instantiate_task(
    cfg: InstantiateConfig, claim: InstantiateClaimItem
) -> InstantiateTask:
    """Pure-python task builder — safe to call outside the retry boundary."""
    work_dir = cfg.output_dir / f"task_{claim.instantiate_hash}"
    return InstantiateTask(
        instantiate_hash=claim.instantiate_hash,
        classify_task_hash=claim.classify_task_hash,
        template_id=claim.template_id,
        work_dir=work_dir,
        stage_dirs={s.name: work_dir / s.name for s in cfg.stages},
    )


def build_prompt(
    cfg: InstantiateConfig, task: InstantiateTask, stage: StepConfig
) -> str:
    """Read ``stage.prompt_file`` and substitute task-level placeholders.

    Uses ``str.format``: the stage-1 prompt uses ``{task_hash}`` to
    parameterise the ``cast.py --seed`` invocation; stage-2 has no
    placeholders.
    """
    raw = stage.prompt_file.read_text(encoding="utf-8")
    return raw.format(
        task_hash=task.instantiate_hash,
        template_id=task.template_id,
        classify_task_hash=task.classify_task_hash,
        diversity_threshold=cfg.diversity_threshold,
    )


def build_instantiation_json(cfg: InstantiateConfig, task: InstantiateTask) -> str:
    """Serialize ``instantiation.json`` contents.

    ``source_file_path`` records the dump-relative path under the file's
    real name. The real filename is discovered from ``_pulled/``; pull
    must have succeeded before this is called (it has, per
    ``stage_final_and_push`` sequencing in ``attempt_instantiate``).
    """
    fp = hashlib.sha256()
    for stage in cfg.stages:
        fp.update(stage.cmd.encode())
        fp.update(b"\x00")
    agent_fp = fp.hexdigest()[:20]

    source_basename = discover_source_file(cfg, task).name
    source_file_path = (
        f"office-files-dump/{task.classify_task_hash[:3]}/"
        f"task_{task.classify_task_hash}/{source_basename}"
    )
    manifest = {
        "task_hash": task.instantiate_hash,
        "template_id": task.template_id,
        "classify_task_hash": task.classify_task_hash,
        "source_file_path": source_file_path,
        "agent_config_fingerprint": agent_fp,
    }
    return json.dumps(manifest, indent=2)


def discover_source_file(cfg: InstantiateConfig, task: InstantiateTask) -> Path:
    """Return the real source-file path inside ``_pulled/``.

    The dump tree convention guarantees exactly one non-metadata file per
    task dir; ``pull_source_files`` excludes ``task.json`` / ``prompt.md``
    / ``.done``, and the classify pull adds a separate ``annotation.md``.
    Anything else in ``_pulled/`` is the source file under its real name
    (e.g. ``Sets.pptx``). Raises ``CommandError`` if discovery is
    ambiguous so retries / operator surface the bug rather than silently
    picking the wrong file. ``cfg`` is unused in the body but kept
    positional for uniformity.
    """
    pulled = task.work_dir / "_pulled"
    candidates = [
        p for p in pulled.iterdir() if p.is_file() and p.name != "annotation.md"
    ]
    if len(candidates) != 1:
        names = sorted(p.name for p in candidates)
        raise CommandError(
            f"discover_source_file (task_{task.instantiate_hash}): "
            f"expected exactly one source file in {pulled}, found {names!r}"
        )
    return candidates[0]


# ── Async helpers ──────────────────────────────────────────────────────


async def pull_source_files(cfg: InstantiateConfig, task: InstantiateTask) -> None:
    """Pull source artifacts in one rsync call.

    The dump dir contains exactly one source file per task plus the
    metadata triple ``task.json`` / ``prompt.md`` / ``.done``. We pull the
    dump dir as a directory with ``--exclude`` filters dropping the
    metadata, plus the classify ``annotation.md`` as a single explicit
    URL. Both land flat in ``task.work_dir / "_pulled"``. Preserving the
    real filename (with extension) is load-bearing for stage-2 dispatch
    — ``python-pptx`` / ``openpyxl`` / ``pdfplumber`` / ``pymupdf`` all
    branch on suffix.
    """
    client = cfg.client
    shard = task.classify_task_hash[:3]
    base = f"rsync://{client.rsync_host}:{client.rsync_port}/artifacts"
    dump_url = (
        f"{base}/office-files-dump/{shard}/"
        f"task_{task.classify_task_hash}/"
    )
    classify_url = (
        f"{base}/office-files-classify/{shard}/"
        f"task_{task.classify_task_hash}/annotation.md"
    )
    dest = task.work_dir / "_pulled"
    dest.mkdir(parents=True, exist_ok=True)
    await run_rsync(
        [
            "-az",
            "--mkpath",
            "--exclude=task.json",
            "--exclude=prompt.md",
            "--exclude=.done",
            dump_url,
            classify_url,
            f"{dest}/",
        ],
        name=f"pull task_{task.instantiate_hash}",
    )


async def prepare_stage_inputs(
    cfg: InstantiateConfig, task: InstantiateTask, stage: StepConfig
) -> None:
    """Build ``<stage>/inputs/`` and ``<stage>/outputs/`` for one stage.

    Self-contained per stage — agents never traverse upward. Static files
    are copied (not symlinked) so each stage's ``inputs/`` is honest.
    ``.venv`` is the exception: large, stable, symlinked.

    Call site has wiped ``stage_dir``; ``mkdir`` flags are non-defensive.
    """
    stage_dir = task.stage_dirs[stage.name]
    inputs = stage_dir / "inputs"
    outputs = stage_dir / "outputs"
    inputs.mkdir(parents=True)
    outputs.mkdir()

    # Pre-create a per-stage trace directory at work_dir top level so cowbox's
    # `--rw {work_dir}/trace_<stage>` directory-level mount has a target. The
    # directory wrapper is required because cowbox bind-mounts only directories,
    # not regular files. Forge writes to `<dir>/trace.jsonl`; stage_final_and_push
    # flattens that back into a single `trace_<stage>.jsonl` file in the artifact
    # tree. Clobbers any prior-attempt content so retries don't accumulate.
    trace_dir = task.work_dir / f"trace_{stage.name}"
    trace_dir.mkdir(exist_ok=True)
    (trace_dir / "trace.jsonl").write_bytes(b"")

    shutil.copy(TEMPLATES_DIR / Path(task.template_id).name, inputs / "metatemplate.md")

    source_src = discover_source_file(cfg, task)
    shutil.copy(source_src, inputs / source_src.name)

    anchor = STAGE_ANCHORS[stage.name]
    shutil.copy(STATIC_DIR / anchor, inputs / anchor)

    if stage.name == "stage1":
        shutil.copy(
            task.work_dir / "_pulled" / "annotation.md",
            inputs / "classify_annotation.md",
        )
        shutil.copy(STATIC_DIR / "cast.py", inputs / "cast.py")
    elif stage.name == "stage2":
        shutil.copy(
            task.stage_dirs["stage1"] / "outputs" / "design_brief.md",
            inputs / "design_brief.md",
        )
    else:
        raise ValidationError(
            f"prepare_stage_inputs: unknown stage {stage.name!r}"
        )

    (inputs / ".venv").symlink_to(VENV_LINK_TARGET)


async def run_stage(
    cfg: InstantiateConfig, task: InstantiateTask, stage: StepConfig
) -> None:
    """Invoke the agent for one stage.

    Raises ``CommandError`` on non-zero exit with full untruncated
    stdout/stderr/returncode. The top-level retry boundary catches every
    exception type uniformly.
    """
    stage_dir = task.stage_dirs[stage.name]
    prompt_text = build_prompt(cfg, task, stage)
    ctx = ExpansionContext(
        work_dir=task.work_dir.resolve(),
        stage_dir=stage_dir.resolve(),
        output_dir=cfg.output_dir.resolve(),
        prompt=prompt_text,
    )
    argv = expand_cmd(stage.cmd, ctx)

    proc = await asyncio.create_subprocess_exec(
        *argv,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    try:
        stdout_b, stderr_b = await asyncio.wait_for(
            proc.communicate(), timeout=stage.timeout
        )
    except TimeoutError:
        proc.kill()
        await proc.wait()
        raise

    if proc.returncode != 0:
        raise CommandError(
            f"{stage.name} (task_{task.instantiate_hash}): "
            f"agent exit {proc.returncode}",
            stdout=stdout_b.decode(errors="replace"),
            stderr=stderr_b.decode(errors="replace"),
            returncode=proc.returncode,
        )


def validate_stage_outputs(
    cfg: InstantiateConfig, task: InstantiateTask, stage: StepConfig
) -> None:
    """File-presence + shape + cast-reproducibility checks.

    Single truth gate per stage. Raises ``ValidationError`` for every
    failed criterion. ``.done`` is criterion #1 (never a skip-validation
    gate).

    Stage 1: ``.done`` + ``design_space.json`` parses +
    ``design_brief.md`` exists + agent's frontmatter matches what
    ``cast.sample_cell`` would produce from the same design_space with
    seed = ``task.instantiate_hash`` (anti-fabrication check).

    Stage 2: ``.done`` + required files ``prompt.md`` / ``rubric.md`` /
    ``deliverable_shape.md`` + a ``reference_files/`` directory (possibly
    empty). Optional ``modifications.md`` / ``completed_work/`` are
    unchecked.

    ``cfg`` is unused in the body but kept positional for uniformity.
    """
    outputs = task.stage_dirs[stage.name] / "outputs"
    if not (outputs / ".done").exists():
        raise ValidationError(f"{stage.name}: .done missing")

    if stage.name == "stage1":
        ds_path = outputs / "design_space.json"
        brief_path = outputs / "design_brief.md"
        if not ds_path.is_file():
            raise ValidationError(
                "stage1: design_space.json missing or malformed"
            )
        try:
            design_space = json.loads(ds_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            raise ValidationError(
                f"stage1: design_space.json malformed — {e}"
            ) from e
        if not brief_path.is_file():
            raise ValidationError("stage1: design_brief.md missing")

        try:
            expected = _run_cast_locally(design_space, task.instantiate_hash)
        except ValueError as e:
            raise ValidationError(
                f"stage1: agent's design_space failed cast: {e}"
            ) from e
        actual = _parse_frontmatter(brief_path.read_text(encoding="utf-8"))
        if expected != actual:
            raise ValidationError(
                "stage1: design_brief frontmatter ≠ cast.py output"
            )
        return

    if stage.name == "stage2":
        for required in STAGE2_REQUIRED_FILES:
            if not (outputs / required).is_file():
                raise ValidationError(f"stage2: {required} missing")
        if not (outputs / "reference_files").is_dir():
            raise ValidationError(
                "stage2: reference_files/ must be a directory"
            )
        return

    raise ValidationError(
        f"validate_stage_outputs: unknown stage {stage.name!r}"
    )


async def stage_final_and_push(
    cfg: InstantiateConfig, task: InstantiateTask
) -> None:
    """Always rebuild ``_final/``, then rsync it to the artifact tree.

    Rebuilding every time means a partial build left by a crashed attempt
    (e.g. ``copytree`` died mid-copy) is never pushed. The ``.pushed``
    marker (checked at the call site) still skips this function entirely
    on retry-after-success; only retry-after-build- or
    retry-after-push-failure re-enters.
    """
    final = task.work_dir / "_final"
    if final.exists():
        shutil.rmtree(final)
    final.mkdir()
    (final / "instantiation.json").write_text(
        build_instantiation_json(cfg, task), encoding="utf-8"
    )
    for stage in cfg.stages:
        src = task.stage_dirs[stage.name] / "outputs"
        shutil.copytree(src, final / stage.name)
        trace_src = task.work_dir / f"trace_{stage.name}" / "trace.jsonl"
        shutil.copy(trace_src, final / f"trace_{stage.name}.jsonl")

    client = cfg.client
    shard = task.instantiate_hash[:3]
    dest = (
        f"rsync://{client.rsync_host}:{client.rsync_port}/artifacts/"
        f"office-files-instantiate/{shard}/task_{task.instantiate_hash}/"
    )
    await run_rsync(
        ["-az", "--mkpath", f"{final}/", dest],
        name=f"push task_{task.instantiate_hash}",
    )


# ── Validation internals ───────────────────────────────────────────────


def _run_cast_locally(design_space: dict, seed: str) -> dict[str, dict]:
    """Re-run ``cast.sample_cell`` in-process.

    cast.py is an importable subpackage member — no sys.path manipulation
    needed.
    """
    from office_files_pipeline.instantiate_static.cast import sample_cell

    return sample_cell(design_space, seed)


def _parse_frontmatter(text: str) -> dict[str, dict]:
    """Parse the YAML frontmatter ``cast._render_brief`` writes.

    The shape is two-deep ("axis: / <indent> key: value") with scalar
    values serialised by ``cast._yaml_scalar``. We parse just that shape
    — cast.py is the only writer of these briefs, so we can match its
    output exactly rather than pulling in a full YAML dependency.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValidationError(
            "stage1: design_brief.md missing opening '---' frontmatter fence"
        )
    try:
        end = lines.index("---", 1)
    except ValueError as e:
        raise ValidationError(
            "stage1: design_brief.md missing closing '---' frontmatter fence"
        ) from e

    result: dict[str, dict] = {}
    current: str | None = None
    for raw in lines[1:end]:
        if not raw.strip():
            continue
        if not raw.startswith("  "):
            stripped = raw.rstrip()
            if not stripped.endswith(":"):
                raise ValidationError(
                    f"stage1: malformed frontmatter axis line: {raw!r}"
                )
            current = stripped[:-1]
            result[current] = {}
            continue
        if current is None:
            raise ValidationError(
                "stage1: frontmatter nested value before any axis name"
            )
        kv = raw.strip()
        if ":" not in kv:
            raise ValidationError(
                f"stage1: malformed frontmatter key-value: {kv!r}"
            )
        key, _, val = kv.partition(":")
        result[current][key.strip()] = _parse_yaml_scalar(val.strip())
    return result


def _parse_yaml_scalar(s: str):
    """Inverse of ``cast._yaml_scalar`` — bool / null / number / quoted str."""
    if s == "true":
        return True
    if s == "false":
        return False
    if s == "null":
        return None
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        return s[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    try:
        if "." in s or "e" in s or "E" in s:
            return float(s)
        return int(s)
    except ValueError:
        return s


# ── Cycle ──────────────────────────────────────────────────────────────


async def attempt_instantiate(
    cfg: InstantiateConfig, task: InstantiateTask
) -> None:
    """One full attempt at the instantiate cycle.

    Idempotent blocks gated by markers:
    - ``.source_pulled`` skips re-pull.
    - Per-stage ``outputs/.done`` skips re-prepare-and-run; validation
      runs UNCONDITIONALLY and wipes ``stage_dir`` on failure (``.done``
      is never a skip-validation gate).
    - ``.pushed`` skips re-push.

    No try/except — exceptions bubble to ``process_one_instantiate``'s
    retry boundary.
    """
    task.work_dir.mkdir(parents=True, exist_ok=True)

    if not (task.work_dir / ".source_pulled").exists():
        await pull_source_files(cfg, task)
        (task.work_dir / ".source_pulled").touch()

    for stage in cfg.stages:
        stage_dir = task.stage_dirs[stage.name]
        if not (stage_dir / "outputs" / ".done").exists():
            shutil.rmtree(stage_dir, ignore_errors=True)
            await prepare_stage_inputs(cfg, task, stage)
            await run_stage(cfg, task, stage)
        try:
            validate_stage_outputs(cfg, task, stage)
        except ValidationError:
            shutil.rmtree(stage_dir, ignore_errors=True)
            raise

    if not (task.work_dir / ".pushed").exists():
        await stage_final_and_push(cfg, task)
        (task.work_dir / ".pushed").touch()

    shutil.rmtree(task.work_dir)


async def process_one_instantiate(
    cfg: InstantiateConfig, task: InstantiateTask
) -> None:
    """Per-task retry loop. All exceptions → JSONL ledger.

    Mirror of ``rollout_cycle.process_one_rollout``. ``retry_with``'s
    ``wait_random(1, 180)`` backoff applies uniformly between attempts.
    ``retryable=(Exception,)`` is explicit for self-documenting code; the
    inner closure handles per-attempt bookkeeping and dumping while
    ``attempt_instantiate`` stays pure happy-path.
    """

    async def _attempt() -> None:
        task.attempt_count += 1
        task.start_ts = time.time()
        try:
            await attempt_instantiate(cfg, task)
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


async def worker_cycle_instantiate(
    cfg: InstantiateConfig, http: httpx.AsyncClient
) -> None:
    """Per-coroutine forever-loop. Spawned ``cfg.concurrency`` times by ``run_instantiate``.

    Claim is in its own try/catch — the coordinator may be restarting
    autossh tunnels and that's not the worker's concern. Empty queues
    sleep-and-continue. Per-task failures are owned by
    ``process_one_instantiate`` (which dumps to JSONL and never propagates).
    """
    while True:
        try:
            claim = await claim_once(
                http, cfg.client, "instantiate", InstantiateClaimItem
            )
        except Exception as e:
            log.warning("claim error: %r; backing off", e)
            await asyncio.sleep(random.uniform(1, 60))
            continue
        if claim is None:
            await asyncio.sleep(random.uniform(1, 60))
            continue
        assert isinstance(claim, InstantiateClaimItem)
        task = build_instantiate_task(cfg, claim)
        log.info("task %s claimed", task.instantiate_hash)
        await process_one_instantiate(cfg, task)


# ── Preflight ──────────────────────────────────────────────────────────


def _check_cowbox_on_path() -> None:
    if shutil.which("cowbox") is None:
        raise RuntimeError(
            "instantiate preflight: 'cowbox' not on PATH — "
            "re-run scripts/remote_launch.sh to populate the workspace venv"
        )


def _check_prompt_file(stage: StepConfig) -> None:
    if not stage.prompt_file.is_file():
        raise RuntimeError(
            f"instantiate preflight: prompt file missing for stage {stage.name!r}: "
            f"{stage.prompt_file}"
        )


def preflight_instantiate(cfg: InstantiateConfig) -> None:
    """Local-only checks; no coordinator/rsync probes."""
    _check_cowbox_on_path()
    for stage in cfg.stages:
        _check_prompt_file(stage)


# ── Entry ──────────────────────────────────────────────────────────────


async def run_instantiate(cfg: InstantiateConfig) -> None:
    """Top-level entry. Wipe output_dir, spawn N workers, gather forever."""
    preflight_instantiate(cfg)
    shutil.rmtree(cfg.output_dir, ignore_errors=True)
    cfg.output_dir.mkdir(parents=True)

    async with httpx.AsyncClient() as http:
        workers = [
            asyncio.create_task(worker_cycle_instantiate(cfg, http))
            for _ in range(cfg.concurrency)
        ]
        await asyncio.gather(*workers, return_exceptions=True)
    log.info("instantiate pipeline complete")
