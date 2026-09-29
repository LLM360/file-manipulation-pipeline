"""Classify-step worker cycle.

Pulls the dump dir for the claimed task, runs the classify agent
against the source file, validates the agent wrote either the full
3-file success bundle (worker-side gate) OR ``.no_file``, then pushes
the explicit output files to ``office-files-classify/<shard>/task_<hash>/``.

Same wipe-and-restart shape as ``rollout_cycle.py`` and
``download_cycle.py``.

Design notes:

- ``pull_source_dir`` uses ``--exclude`` filters so the agent's working
  directory contains only ``task.json`` + the source file. A stale
  ``prompt.md``, the dump-side ``.done``, and any pre-existing classify
  outputs from a stale push are filtered out at pull time. This keeps
  the agent's view clean and uniform regardless of what's in the artifact tree.
- ``push_classify`` success path pushes ONLY ``assignments.json`` and
  ``annotation.md`` (NOT ``.done_classify``). The ``.done_classify`` marker
  is the agent's self-attestation that it completed the work — the worker
  still gates on it in ``validate_classify`` — but it does not need to
  appear in the artifact tree, since downstream rebuild validators check for the
  actual artifacts.
"""
from __future__ import annotations

import asyncio
import json
import logging
import random
import shutil
import time
from dataclasses import dataclass
from importlib.resources import files
from pathlib import Path

import httpx
import jsonschema
from pydantic import BaseModel
from tenacity import RetryError, stop_after_attempt

from office_files_pipeline.config import ClassifyConfig, StepConfig
from office_files_pipeline.expand import ExpansionContext, expand_cmd
from office_files_pipeline.failures import CommandError, ValidationError, dump_failure
from office_files_pipeline.remote import claim_once, run_rsync
from office_files_pipeline.retry import retry_with

log = logging.getLogger("ofpipe.classify")


# ── Module constants (resolved once at import via importlib.resources) ─

_PACKAGE_ROOT = Path(str(files("office_files_pipeline")))
TEMPLATES_DIR = _PACKAGE_ROOT / "metatemplates" / "task_types"
_SCHEMA_PATH = _PACKAGE_ROOT / "schemas" / "assignments.schema.json"
SCHEMA_TEXT = _SCHEMA_PATH.read_text(encoding="utf-8")
SCHEMA_VALIDATOR = jsonschema.Draft202012Validator(json.loads(SCHEMA_TEXT))

# Template IDs are ``task_types/<basename>.md`` (relative to ``metatemplates/``).
KNOWN_TEMPLATE_IDS: frozenset[str] = frozenset(
    f"task_types/{p.name}" for p in TEMPLATES_DIR.glob("*.md")
)


# ── Types ──────────────────────────────────────────────────────────────


class ClassifyClaimItem(BaseModel):
    """Claim payload from ``POST /claim/classify``.

    Mirrors ``pipeline_coordinator/api.py::ClassifyClaimItem``.
    """

    task_hash: str


@dataclass
class ClassifyTask:
    """Per-claim runtime state. Mutable. ``cfg`` is NOT a field."""

    task_hash: str
    work_dir: Path
    start_ts: float = 0.0
    attempt_count: int = 0


# ── Builders ───────────────────────────────────────────────────────────


def build_classify_task(cfg: ClassifyConfig, claim: ClassifyClaimItem) -> ClassifyTask:
    """Pure-python builder; safe outside any retry boundary."""
    return ClassifyTask(
        task_hash=claim.task_hash,
        work_dir=cfg.output_dir / f"task_{claim.task_hash}",
    )


def build_prompt(cfg: ClassifyConfig, task: ClassifyTask, stage: StepConfig) -> str:
    """Read prompt template and substitute placeholders.

    Uses ``str.replace`` (NOT ``str.format``) because ``{schema_json}``
    is a multi-line JSON document that contains literal ``{`` and ``}``
    characters; ``.format()`` would interpret them as format specifiers
    and crash.

    Placeholders:

    - ``{schema_json}``: full JSON schema for assignments.json (multi-line)
    - ``{templates_dir}``: absolute path to metatemplates/task_types/
    - ``{task_filename}``: basename of the source file (from task.json's file_path)
    """
    raw = stage.prompt_file.read_text(encoding="utf-8")
    task_data = json.loads((task.work_dir / "task.json").read_text(encoding="utf-8"))
    task_filename = Path(task_data["file_path"]).name

    result = raw
    result = result.replace("{schema_json}", SCHEMA_TEXT)
    result = result.replace("{templates_dir}", str(TEMPLATES_DIR))
    result = result.replace("{task_filename}", task_filename)
    return result


# ── Cycle phases ───────────────────────────────────────────────────────


async def pull_source_dir(cfg: ClassifyConfig, task: ClassifyTask) -> None:
    """rsync the dump dir into work_dir, excluding all metadata files.

    A whole-dir pull would leave a stale ``prompt.md`` and the download
    marker ``.done`` in the agent's working directory. We exclude them —
    and also any classify-side outputs from an over-pushed stale dir — so
    the agent sees exactly two things: ``task.json`` and the source file.

    ``rebuild_classify`` only puts hashes-with-real-file in the eligible
    set, so dump dirs with ``.no_file`` are NOT claim-able as classify
    tasks; this function will always pull a dir containing the actual
    source file.
    """
    shard = task.task_hash[:3]
    src = (
        f"rsync://{cfg.client.rsync_host}:{cfg.client.rsync_port}/"
        f"artifacts/office-files-dump/{shard}/task_{task.task_hash}/"
    )
    task.work_dir.mkdir(parents=True, exist_ok=True)
    await run_rsync(
        [
            "-az",
            "--exclude=prompt.md",
            "--exclude=.done",
            "--exclude=.done_classify",
            "--exclude=.no_file",
            "--exclude=annotation.md",
            "--exclude=assignments.json",
            src,
            f"{task.work_dir}/",
        ],
        name=f"pull task_{task.task_hash}",
    )


async def run_stage(cfg: ClassifyConfig, task: ClassifyTask, stage: StepConfig) -> None:
    """Invoke the classify agent for one stage."""
    prompt_text = build_prompt(cfg, task, stage)
    ctx = ExpansionContext(
        work_dir=task.work_dir.resolve(),
        stage_dir=task.work_dir.resolve(),  # classify has no per-stage subdir
        output_dir=cfg.output_dir.resolve(),
        prompt=prompt_text,
    )
    argv = expand_cmd(stage.cmd, ctx)

    proc = await asyncio.create_subprocess_exec(
        *argv,
        stdin=asyncio.subprocess.DEVNULL,
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
            f"classify (task_{task.task_hash}): forge exit {proc.returncode}",
            stdout=stdout_b.decode(errors="replace"),
            stderr=stderr_b.decode(errors="replace"),
            returncode=proc.returncode,
        )


def _normalize_template_id(tid: str) -> str | None:
    """Canonicalize ``tid`` to ``task_types/<basename>.md`` or return ``None``.

    Accepts any spelling whose final path segment matches a known template
    basename — absolute paths, bare basenames, over-qualified relative
    paths, and missing ``.md`` suffix all collapse to the canonical form
    in ``KNOWN_TEMPLATE_IDS``. Returns ``None`` for genuine unknowns
    (hallucinated names) so the caller raises.
    """
    basename = Path(tid.strip()).name
    if not basename.endswith(".md"):
        basename += ".md"
    canonical = f"task_types/{basename}"
    return canonical if canonical in KNOWN_TEMPLATE_IDS else None


def validate_classify(cfg: ClassifyConfig, task: ClassifyTask) -> str:
    """Validate the agent's terminal state. Returns 'success' or 'no_file'.

    Two valid terminal states:

    1. ``.no_file`` exists — agent gave up (rare: source file missing
       or unreadable; mostly unreachable since ``rebuild_classify``
       excludes no-file dump tasks, but kept as a safety valve).
    2. ``.done_classify`` exists AND ``assignments.json`` parses + validates
       against the JSON schema + every ``template_id`` ∈ KNOWN_TEMPLATE_IDS,
       AND ``annotation.md`` exists.

    Note: ``.done_classify`` is the agent's self-attestation that it
    completed the work; we use it as a worker-side gate even though we
    do not push it to the artifact tree (the rebuild validator gates on the
    actual artifacts ``assignments.json`` + ``annotation.md`` instead).

    Anything else → ValidationError.

    ``cfg`` unused; kept positional for uniformity.
    """
    if (task.work_dir / ".no_file").exists():
        return "no_file"

    if not (task.work_dir / ".done_classify").exists():
        raise ValidationError(
            f"task_{task.task_hash}: no terminal marker "
            f"(neither .done_classify nor .no_file)"
        )

    assignments_path = task.work_dir / "assignments.json"
    try:
        assignments = json.loads(assignments_path.read_text(encoding="utf-8"))
    except FileNotFoundError as e:
        raise ValidationError(
            f"task_{task.task_hash}: assignments.json missing"
        ) from e
    except json.JSONDecodeError as e:
        raise ValidationError(
            f"task_{task.task_hash}: assignments.json malformed — {e}"
        ) from e

    errors = list(SCHEMA_VALIDATOR.iter_errors(assignments))
    if errors:
        raise ValidationError(
            f"task_{task.task_hash}: assignments.json schema violation — "
            f"{errors[0].message}"
        )

    for entry in assignments["assignments"]:
        tid = entry["template_id"]
        canonical = _normalize_template_id(tid)
        if canonical not in KNOWN_TEMPLATE_IDS:
            raise ValidationError(
                f"task_{task.task_hash}: unknown template_id {tid!r}"
            )
        entry["template_id"] = canonical
    
    assignments_path.write_text(json.dumps(assignments, indent=2), encoding="utf-8")

    if not (task.work_dir / "annotation.md").exists():
        raise ValidationError(
            f"task_{task.task_hash}: annotation.md missing"
        )

    return "success"


async def push_classify(cfg: ClassifyConfig, task: ClassifyTask, outcome: str) -> None:
    """rsync explicit output files to office-files-classify/<shard>/task_<hash>/.

    The success path pushes ONLY ``assignments.json`` and
    ``annotation.md`` — the ``.done_classify`` marker stays local
    (worker self-attestation only). The rebuild validator gates on
    ``assignments.json`` AND ``annotation.md`` presence; pushing
    ``annotation.md`` LAST guarantees that any rebuild scan racing a
    partial push either sees neither file (push hasn't progressed past
    assignments) or both (push complete).

    ``outcome`` is the return value of ``validate_classify``:

    - ``"success"``: pushes assignments.json (first) then annotation.md (last)
    - ``"no_file"``: pushes .no_file only
    """
    shard = task.task_hash[:3]
    dst = (
        f"rsync://{cfg.client.rsync_host}:{cfg.client.rsync_port}/"
        f"artifacts/office-files-classify/{shard}/task_{task.task_hash}/"
    )

    if outcome == "no_file":
        await run_rsync(
            ["-az", "--mkpath", str(task.work_dir / ".no_file"), dst + ".no_file"],
            name=f"push .no_file task_{task.task_hash}",
        )
        return

    # Success path: assignments.json first, annotation.md last (gating signal).
    await run_rsync(
        [
            "-az", "--mkpath",
            str(task.work_dir / "assignments.json"), dst + "assignments.json",
        ],
        name=f"push assignments task_{task.task_hash}",
    )
    await run_rsync(
        ["-az", str(task.work_dir / "annotation.md"), dst + "annotation.md"],
        name=f"push annotation task_{task.task_hash}",
    )


async def attempt_classify(cfg: ClassifyConfig, task: ClassifyTask) -> None:
    """One full attempt: wipe → pull → run → validate → push → cleanup."""
    if task.work_dir.exists():
        shutil.rmtree(task.work_dir)

    await pull_source_dir(cfg, task)
    await run_stage(cfg, task, cfg.stages[0])
    outcome = validate_classify(cfg, task)
    await push_classify(cfg, task, outcome)

    shutil.rmtree(task.work_dir)


async def process_one_classify(cfg: ClassifyConfig, task: ClassifyTask) -> None:
    """Per-task retry loop. Mirror of process_one_download."""

    async def _attempt() -> None:
        task.attempt_count += 1
        task.start_ts = time.time()
        try:
            await attempt_classify(cfg, task)
        except Exception as exc:
            dump_failure(cfg, task, exc)
            raise

    try:
        await retry_with(
            _attempt,
            stop=stop_after_attempt(cfg.max_retries),
            retryable=(Exception,),
            name=f"task {task.task_hash}",
        )
        log.info(
            "task %s succeeded in attempt %d (elapsed %.1fs)",
            task.task_hash, task.attempt_count, time.time() - task.start_ts,
        )
    except RetryError:
        log.error(
            "task %s exhausted %d attempts",
            task.task_hash, cfg.max_retries,
        )


async def worker_cycle_classify(
    cfg: ClassifyConfig, http: httpx.AsyncClient
) -> None:
    """Per-coroutine forever-loop. Mirror of worker_cycle_download."""
    while True:
        try:
            claim = await claim_once(http, cfg.client, "classify", ClassifyClaimItem)
        except Exception as e:
            log.warning("claim error: %r; backing off", e)
            await asyncio.sleep(random.uniform(1, 60))
            continue
        if claim is None:
            await asyncio.sleep(random.uniform(1, 60))
            continue
        assert isinstance(claim, ClassifyClaimItem)
        task = build_classify_task(cfg, claim)
        log.info("task %s claimed", task.task_hash)
        await process_one_classify(cfg, task)


# ── Preflight ──────────────────────────────────────────────────────────


def _check_prompt_file(stage: StepConfig) -> None:
    if stage.prompt_file is None or not stage.prompt_file.is_file():
        raise RuntimeError(
            f"classify preflight: prompt file missing for stage {stage.name!r}: "
            f"{stage.prompt_file}"
        )


def _check_templates_loaded() -> None:
    if not KNOWN_TEMPLATE_IDS:
        raise RuntimeError(
            f"classify preflight: no metatemplates loaded from {TEMPLATES_DIR} — "
            f"directory missing or empty"
        )


def _check_uv_cache_dir() -> None:
    cache = Path("/root/.cache/uv")
    cache.mkdir(parents=True, exist_ok=True)


def preflight_classify(cfg: ClassifyConfig) -> None:
    """Local-only checks; no coordinator/rsync probes."""
    for stage in cfg.stages:
        _check_prompt_file(stage)
    _check_templates_loaded()
    _check_uv_cache_dir()


# ── Entry ──────────────────────────────────────────────────────────────


async def run_classify(cfg: ClassifyConfig) -> None:
    """Top-level entry. Wipe output_dir, spawn N workers, gather forever."""
    preflight_classify(cfg)
    shutil.rmtree(cfg.output_dir, ignore_errors=True)
    cfg.output_dir.mkdir(parents=True)

    async with httpx.AsyncClient() as http:
        workers = [
            asyncio.create_task(worker_cycle_classify(cfg, http))
            for _ in range(cfg.concurrency)
        ]
        await asyncio.gather(*workers, return_exceptions=True)
    log.info("classify pipeline complete")
