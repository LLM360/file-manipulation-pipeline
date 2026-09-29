"""Shared failure types and JSONL ledger dumper.

One ``CommandError`` for any subprocess (agent CLI, rsync) non-zero
exit; one ``ValidationError`` for output-gate failures; one
``dump_failure(cfg, task, exc)`` that writes a single JSONL record per
attempt with the full untruncated streams. The ``step`` field on each
record (sourced from ``cfg.step``) keeps records distinguishable when
several steps share one ``cfg.failure_log_path``.
"""
from __future__ import annotations

import json
import time
import traceback
from typing import Any


class CommandError(RuntimeError):
    """Any subprocess (agent CLI, rsync) non-zero exit. Carries full
    untruncated streams + returncode for the JSONL ledger.
    """

    def __init__(
        self,
        msg: str,
        *,
        stdout: str | None = None,
        stderr: str | None = None,
        returncode: int | None = None,
    ):
        super().__init__(msg)
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode


class ValidationError(RuntimeError):
    """Output-gate failures (missing files, frontmatter mismatch, stage
    not done, etc.). No extra attrs — the message names what was wrong.
    """


def dump_failure(cfg: Any, task: Any, exc: Exception) -> None:
    """Append one per-attempt failure record to ``cfg.failure_log_path``.

    Reads ``cfg.step`` for cross-step distinguishability. Reads
    ``stdout`` / ``stderr`` / ``returncode`` from ``exc`` via ``getattr`` —
    populated by ``CommandError``; ``ValidationError`` and bare exceptions
    get ``None``. Always captures the active traceback.
    """
    record = {
        "ts": time.time(),
        "step": cfg.step,
        "task_hash": task.task_hash,
        "attempt": task.attempt_count,
        "elapsed_s": time.time() - task.start_ts,
        "exception_type": type(exc).__name__,
        "exception_message": str(exc),
        "exception_traceback": traceback.format_exc(),
        "stdout": getattr(exc, "stdout", None),
        "stderr": getattr(exc, "stderr", None),
        "returncode": getattr(exc, "returncode", None),
    }
    with cfg.failure_log_path.open("a") as f:
        f.write(json.dumps(record) + "\n")
