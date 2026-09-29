"""Download-step worker cycle.

Mirrors rollout_cycle.py's wipe-and-restart shape. The agent fetches
a single file from the web using ``task.raw_url`` (and writes either
``.done`` with the file path on success, or ``.no_file`` on intentional
skip — e.g. file >100MB). The worker validates which terminal marker
the agent produced, then rsync-pushes the entire work_dir to
``office-files-dump/<shard>/task_<hash>/`` in the artifact tree.

Conventions shared with the other step cycles:

- ``cfg`` flows positionally everywhere (no field on the task dataclass).
- Single top-level retry boundary in ``process_one_download``;
  ``retryable=(Exception,)`` catches all exception types uniformly.
- Subprocess non-zero exit raises ``CommandError`` with full untruncated
  stdout/stderr/returncode.
- Validation failures raise ``ValidationError``; the wipe at the start
  of the next attempt resets state.
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
import time
from dataclasses import dataclass
from pathlib import Path

import httpx
from pydantic import BaseModel
from tenacity import RetryError, stop_after_attempt

from office_files_pipeline.config import DownloadConfig, StepConfig
from office_files_pipeline.expand import ExpansionContext, expand_cmd
from office_files_pipeline.failures import CommandError, ValidationError, dump_failure
from office_files_pipeline.remote import claim_once, run_rsync
from office_files_pipeline.retry import retry_with

log = logging.getLogger("ofpipe.download")


# ── Types ──────────────────────────────────────────────────────────────


class DownloadClaimItem(BaseModel):
    """Claim payload from ``POST /claim/download``.

    Mirrors ``pipeline_coordinator/api.py::DownloadClaimItem``. ``row`` is
    the full parquet row as a dict (``raw_url``, ``file_path``,
    ``file_ext``, ``repo_full_name``, etc.).
    """

    idx: int
    row: dict


@dataclass
class DownloadTask:
    """Per-claim runtime state. Mutable. ``cfg`` is NOT a field — passed
    as the first positional arg everywhere (uniform with rollout/instantiate).
    """

    task_hash: str         # sha256(row["raw_url"])[:20]
    idx: int               # parquet row idx (for logging / failure context)
    raw_url: str           # extracted from row
    file_path: str         # extracted from row (gives downloaded filename via Path(...).name)
    row: dict              # full row, dumped to task.json verbatim
    work_dir: Path
    start_ts: float = 0.0
    attempt_count: int = 0


# ── Builders ───────────────────────────────────────────────────────────


def _row_task_hash(raw_url: str) -> str:
    """Match the coordinator's hash convention (rebuild.py::_row_task_hash)."""
    return hashlib.sha256(raw_url.encode()).hexdigest()[:20]


def build_download_task(cfg: DownloadConfig, claim: DownloadClaimItem) -> DownloadTask:
    """Pure-python builder; safe outside any retry boundary."""
    raw_url = claim.row["raw_url"]
    task_hash = _row_task_hash(raw_url)
    return DownloadTask(
        task_hash=task_hash,
        idx=claim.idx,
        raw_url=raw_url,
        file_path=claim.row["file_path"],
        row=claim.row,
        work_dir=cfg.output_dir / f"task_{task_hash}",
    )


def build_prompt(cfg: DownloadConfig, task: DownloadTask, stage: StepConfig) -> str:
    """Read prompt template and substitute per-task placeholders.

    Uses ``str.replace`` (NOT ``str.format``) so any literal ``{``/``}``
    in the prompt body — JSON examples, bash ``${VAR}`` references, code
    samples, markdown braces — survives untouched. Only the three
    explicit token strings below are rewritten. Mirrors classify_cycle's
    pattern.

    Placeholders supported:

    - ``{raw_url}``: the URL to download from
    - ``{file_path}``: original GitHub-relative path (gives the filename)
    - ``{max_size_mb}``: skip threshold (currently 100)
    """
    raw = stage.prompt_file.read_text(encoding="utf-8")
    result = raw
    result = result.replace("{raw_url}", task.raw_url)
    result = result.replace("{file_path}", task.file_path)
    result = result.replace("{max_size_mb}", "100")
    return result


# ── Cycle phases ───────────────────────────────────────────────────────


async def prepare_download(cfg: DownloadConfig, task: DownloadTask) -> None:
    """Create work_dir and write task.json.

    ``task.json`` is required downstream by classify (which reads
    ``file_path`` to derive ``task_filename``). Worker writes it BEFORE
    the agent runs so the agent doesn't have to.
    """
    task.work_dir.mkdir(parents=True)
    (task.work_dir / "task.json").write_text(
        json.dumps(task.row, default=str, indent=2),
        encoding="utf-8",
    )


async def run_stage(cfg: DownloadConfig, task: DownloadTask, stage: StepConfig) -> None:
    """Invoke the download agent for one stage.

    Raises ``CommandError`` on non-zero exit with full untruncated streams.
    No retryable_patterns — top-level retry boundary catches every
    exception type uniformly.
    """
    prompt_text = build_prompt(cfg, task, stage)
    ctx = ExpansionContext(
        work_dir=task.work_dir.resolve(),
        stage_dir=task.work_dir.resolve(),  # download has no per-stage subdir
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
            f"download (task_{task.task_hash}, idx={task.idx}): forge exit {proc.returncode}",
            stdout=stdout_b.decode(errors="replace"),
            stderr=stderr_b.decode(errors="replace"),
            returncode=proc.returncode,
        )


# Files the agent / worker creates that are NOT the downloaded artifact.
# Used for "is there a real file?" check during validation.
_DOWNLOAD_METADATA_NAMES = frozenset({"task.json", ".done", ".no_file"})


def validate_download(cfg: DownloadConfig, task: DownloadTask) -> None:
    """Validate which terminal marker the agent wrote and that it's consistent.

    Two valid terminal states:

    1. ``.no_file`` exists — agent intentionally skipped (e.g. >100MB).
       No real file expected. PUSH still happens so the artifact tree has the
       marker (otherwise rebuild would re-eligible the task).
    2. ``.done`` exists AND a non-metadata file is present — agent
       successfully downloaded.

    Anything else is broken — raise ValidationError so the next attempt
    starts fresh.

    cfg unused; kept positional for uniformity with other steps.
    """
    has_no_file = (task.work_dir / ".no_file").exists()
    has_done = (task.work_dir / ".done").exists()

    if has_no_file:
        # Both markers contradict each other: the attempt is invalid, and the
        # retry starts from a wiped work_dir.
        if has_done:
            raise ValidationError(
                f"task_{task.task_hash}: agent wrote both .no_file and .done; attempt is invalid"
            )
        return

    if not has_done:
        raise ValidationError(
            f"task_{task.task_hash}: neither .done nor .no_file present "
            f"after agent run (work_dir contents: "
            f"{sorted(p.name for p in task.work_dir.iterdir())})"
        )

    # .done present — verify a real file is in the dir.
    real_files = [
        p for p in task.work_dir.iterdir()
        if p.is_file() and p.name not in _DOWNLOAD_METADATA_NAMES
    ]
    if not real_files:
        raise ValidationError(
            f"task_{task.task_hash}: .done present but no downloaded file. "
            f"Agent must either (a) write the file alongside .done, or "
            f"(b) write .no_file instead of .done. work_dir contents: "
            f"{sorted(p.name for p in task.work_dir.iterdir())}"
        )


async def push_download(cfg: DownloadConfig, task: DownloadTask) -> None:
    """rsync the entire work_dir to office-files-dump/<shard>/task_<hash>/.

    Whole-dir push is intentional: the artifact tree receives task.json + the
    downloaded file (or .no_file) + .done in one operation. ``--mkpath``
    creates intermediate shard dirs as needed.
    """
    shard = task.task_hash[:3]
    dst = (
        f"rsync://{cfg.client.rsync_host}:{cfg.client.rsync_port}/"
        f"artifacts/office-files-dump/{shard}/task_{task.task_hash}/"
    )
    await run_rsync(
        ["-az", "--mkpath", f"{task.work_dir}/", dst],
        name=f"push task_{task.task_hash}",
    )


async def attempt_download(cfg: DownloadConfig, task: DownloadTask) -> None:
    """One full attempt: wipe → prepare → run agent → validate → push → cleanup.

    No try/except — exceptions bubble to ``process_one_download``'s retry
    boundary, which dumps to JSONL and triggers the next attempt.
    """
    if task.work_dir.exists():
        shutil.rmtree(task.work_dir)

    await prepare_download(cfg, task)
    await run_stage(cfg, task, cfg.stages[0])
    validate_download(cfg, task)
    await push_download(cfg, task)

    shutil.rmtree(task.work_dir)


async def process_one_download(cfg: DownloadConfig, task: DownloadTask) -> None:
    """Per-task retry loop. All exceptions → JSONL ledger.

    Uses ``retry_with`` so step inherits the ``wait_random(1, 180)``
    backoff between attempts. ``retryable=(Exception,)`` is explicit
    for self-documenting code.
    """

    async def _attempt() -> None:
        task.attempt_count += 1
        task.start_ts = time.time()
        try:
            await attempt_download(cfg, task)
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
            "task %s (idx=%d) succeeded in attempt %d (elapsed %.1fs)",
            task.task_hash, task.idx, task.attempt_count,
            time.time() - task.start_ts,
        )
    except RetryError:
        log.error(
            "task %s (idx=%d) exhausted %d attempts",
            task.task_hash, task.idx, cfg.max_retries,
        )


async def worker_cycle_download(
    cfg: DownloadConfig, http: httpx.AsyncClient
) -> None:
    """Per-coroutine forever-loop. Spawned ``cfg.concurrency`` times by run_download.

    Claim is in its own try/catch — coordinator may be restarting tunnels
    and that's not the worker's concern. Empty queues sleep-and-continue.
    """
    while True:
        try:
            claim = await claim_once(http, cfg.client, "download", DownloadClaimItem)
        except Exception as e:
            log.warning("claim error: %r; backing off", e)
            await asyncio.sleep(random.uniform(1, 60))
            continue
        if claim is None:
            await asyncio.sleep(random.uniform(1, 60))
            continue
        assert isinstance(claim, DownloadClaimItem)
        task = build_download_task(cfg, claim)
        log.info("task %s (idx=%d) claimed", task.task_hash, task.idx)
        await process_one_download(cfg, task)


# ── Preflight (kept minimal; rollout_cycle.preflight_rollout pattern) ──


def _check_prompt_file(stage: StepConfig) -> None:
    if stage.prompt_file is None or not stage.prompt_file.is_file():
        raise RuntimeError(
            f"download preflight: prompt file missing for stage {stage.name!r}: "
            f"{stage.prompt_file}"
        )


def _check_uv_cache_dir() -> None:
    """cowbox's --rw of a non-existent path can be silently odd; mkdir is cheap insurance."""
    cache = Path("/root/.cache/uv")
    cache.mkdir(parents=True, exist_ok=True)


def preflight_download(cfg: DownloadConfig) -> None:
    """Local-only checks; no coordinator/rsync probes."""
    for stage in cfg.stages:
        _check_prompt_file(stage)
    _check_uv_cache_dir()


# ── Entry ──────────────────────────────────────────────────────────────


async def run_download(cfg: DownloadConfig) -> None:
    """Top-level entry. Wipe output_dir, spawn N workers, gather forever."""
    preflight_download(cfg)
    shutil.rmtree(cfg.output_dir, ignore_errors=True)
    cfg.output_dir.mkdir(parents=True)

    async with httpx.AsyncClient() as http:
        workers = [
            asyncio.create_task(worker_cycle_download(cfg, http))
            for _ in range(cfg.concurrency)
        ]
        await asyncio.gather(*workers, return_exceptions=True)
    log.info("download pipeline complete")
