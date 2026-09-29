"""StageState + AppRuntime — the coordinator's in-memory state surface.

``StageState`` is the per-stage mutable work ledger. ``AppRuntime``
bundles app-scoped runtime data (the loaded parquet) with the per-stage
ledgers, so one object flows from ``__main__`` into ``create_app``.
"""

from collections import deque
from dataclasses import dataclass, field

import polars as pl

from pipeline_coordinator.reconciler import TunnelReconciler


@dataclass
class StageState:
    # ``download``, ``classify`` and ``rollout`` use a ``set`` (constant-time
    # arbitrary pop). ``instantiate`` uses an ordered ``deque`` of
    # ``(file_ext, template_id, classify_task_hash)`` tuples so that the
    # greedy marginal balancing order is preserved at popleft time.
    eligible: set[int | str] | deque = field(default_factory=set)


@dataclass
class AppRuntime:
    """App-scoped runtime state shared by rebuilders and request handlers.

    ``parquet`` is immutable reference data loaded once at startup and
    reused by the ``/claim/download`` hot path and ``rebuild_instantiate``.
    ``stages`` is the registry of per-stage mutable ledgers.
    ``reconciler`` is the autossh supervisor; ``POST /workers`` reaches
    it via this field.
    """

    parquet: pl.DataFrame
    stages: dict[str, StageState]
    reconciler: TunnelReconciler
