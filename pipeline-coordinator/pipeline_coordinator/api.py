"""FastAPI app factory for the pipeline coordinator.

The per-stage claim and rebuild endpoints are written out explicitly;
there is no stage-plugin abstraction.

Endpoints:

* ``POST /claim/{download,classify,rollout}`` — constant-time
  ``set.pop()``; rollout skips hashes whose output dir already exists.
* ``POST /claim/instantiate``    — FIFO ``deque.popleft()`` over the
  balanced queue, skipping items whose output dir already exists.
* ``POST /rebuild/{stage}``      — synchronous filesystem rescan; replaces
  the stage's ``eligible`` container in place. Blocks the event loop by
  design.
* ``POST /workers``              — register a worker IP; opens its tunnels.
* ``GET /health``                — liveness probe.

Stages are looked up in a dict populated by the factory; an unknown stage
is a 404.
"""

from __future__ import annotations

from collections import deque
from typing import Callable

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .config import CoordinatorConfig, INSTANTIATE_SUBDIR, ROLLOUT_SUBDIR
from .rebuild import (
    instantiate_hash_for,
    rebuild_classify,
    rebuild_download,
    rebuild_instantiate,
    rebuild_rollout,
)
from .state import AppRuntime, StageState


class DownloadClaimItem(BaseModel):
    idx: int
    row: dict


class ClassifyClaimItem(BaseModel):
    task_hash: str


class InstantiateClaimItem(BaseModel):
    """Claim payload; matches the worker-side model."""

    template_id: str
    classify_task_hash: str
    instantiate_hash: str


class DownloadClaimResponse(BaseModel):
    task: DownloadClaimItem | None


class ClassifyClaimResponse(BaseModel):
    task: ClassifyClaimItem | None


class InstantiateClaimResponse(BaseModel):
    task: InstantiateClaimItem | None


class RolloutClaimItem(BaseModel):
    """Claim payload; matches the worker-side model."""

    instantiate_hash: str


class RolloutClaimResponse(BaseModel):
    task: RolloutClaimItem | None


class RebuildResponse(BaseModel):
    counts: dict[str, int]


class WorkerRegister(BaseModel):
    """``POST /workers`` payload."""

    ip: str


def create_app(cfg: CoordinatorConfig, runtime: AppRuntime) -> FastAPI:
    """Build a FastAPI app wired to the ``AppRuntime``.

    ``runtime.stages`` must contain keys ``"download"``, ``"classify"``,
    ``"instantiate"`` and ``"rollout"``. Rebuilds mutate the existing
    ``StageState`` instances in place so callers that hold references keep
    seeing fresh data.
    """
    app = FastAPI()

    rebuilders: dict[str, Callable[[], StageState]] = {
        "download": lambda: rebuild_download(cfg, runtime.parquet),
        "classify": lambda: rebuild_classify(cfg),
        "instantiate": lambda: rebuild_instantiate(cfg, runtime.parquet),
        "rollout": lambda: rebuild_rollout(cfg),
    }

    def _get_state(stage: str) -> StageState:
        try:
            return runtime.stages[stage]
        except KeyError:
            raise HTTPException(status_code=404, detail=f"unknown stage {stage!r}")

    @app.get("/health")
    def health() -> dict[str, bool]:
        return {"ok": True}

    @app.post("/workers", status_code=204)
    async def register_worker(payload: WorkerRegister) -> None:
        """Register a remote worker IP and start its reverse tunnels.

        Idempotent — re-registering the same IP while autossh is alive
        is a no-op; a new ``_supervise`` task only spawns when the prior
        one has finished (autossh exited or task cancelled).

        ``async`` so the handler runs on the event loop;
        ``reconciler.register`` calls ``asyncio.create_task`` which needs
        a running loop in the calling thread.
        """
        runtime.reconciler.register(payload.ip)

    @app.post("/claim/download", response_model=DownloadClaimResponse)
    def claim_download() -> DownloadClaimResponse:
        state = _get_state("download")
        try:
            idx = state.eligible.pop()
        except KeyError:
            return DownloadClaimResponse(task=None)
        row = runtime.parquet.row(int(idx), named=True)
        return DownloadClaimResponse(task=DownloadClaimItem(idx=int(idx), row=row))

    @app.post("/claim/classify", response_model=ClassifyClaimResponse)
    def claim_classify() -> ClassifyClaimResponse:
        state = _get_state("classify")
        try:
            task_hash = state.eligible.pop()
        except KeyError:
            return ClassifyClaimResponse(task=None)
        return ClassifyClaimResponse(task=ClassifyClaimItem(task_hash=str(task_hash)))

    @app.post("/claim/instantiate", response_model=InstantiateClaimResponse)
    def claim_instantiate() -> InstantiateClaimResponse:
        """FIFO popleft + skip-on-pop check.

        Pops items from the greedy-balanced queue; for each, computes the
        ``instantiate_hash`` and skips if
        ``office-files-instantiate/<shard>/task_<instantiate_hash>/``
        already exists on disk. Filesystem is the source of truth — the
        queue is ephemeral and loses identity across rebuilds.
        """
        state = _get_state("instantiate")
        queue = state.eligible
        if not isinstance(queue, deque):
            raise HTTPException(
                status_code=500,
                detail="instantiate state is not a deque — rebuild required",
            )
        while queue:
            _file_ext, template_id, classify_task_hash = queue.popleft()
            instantiate_hash = instantiate_hash_for(template_id, classify_task_hash)
            shard = instantiate_hash[:3]
            existing = (
                cfg.base_dir
                / INSTANTIATE_SUBDIR
                / shard
                / f"task_{instantiate_hash}"
            )
            if existing.exists():
                continue
            return InstantiateClaimResponse(
                task=InstantiateClaimItem(
                    template_id=template_id,
                    classify_task_hash=classify_task_hash,
                    instantiate_hash=instantiate_hash,
                )
            )
        return InstantiateClaimResponse(task=None)

    @app.post("/claim/rollout", response_model=RolloutClaimResponse)
    def claim_rollout() -> RolloutClaimResponse:
        """Pop an instantiate hash; skip if the rollout dir already exists
        (race with a concurrent worker). Filesystem is the source of truth
        — the eligible set loses identity across rebuilds.
        """
        state = _get_state("rollout")
        while state.eligible:
            try:
                h = state.eligible.pop()
            except KeyError:
                break
            shard = str(h)[:3]
            existing = (
                cfg.base_dir
                / ROLLOUT_SUBDIR
                / shard
                / f"task_{h}"
            )
            if existing.exists():
                continue
            return RolloutClaimResponse(
                task=RolloutClaimItem(instantiate_hash=str(h))
            )
        return RolloutClaimResponse(task=None)

    @app.post("/rebuild/{stage}", response_model=RebuildResponse)
    def rebuild(stage: str) -> RebuildResponse:
        state = _get_state(stage)
        try:
            rebuilder = rebuilders[stage]
        except KeyError:
            raise HTTPException(status_code=404, detail=f"unknown stage {stage!r}")
        fresh = rebuilder()
        state.eligible = fresh.eligible
        return RebuildResponse(counts={"eligible": len(state.eligible)})

    return app
