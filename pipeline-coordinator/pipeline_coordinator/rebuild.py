"""Synchronous filesystem scans that produce fresh StageState.

Rebuilds block the event loop by design. ``walk_task_hashes`` and the
marker walkers shell out to ``xargs -P 32 find`` for ~30x I/O parallelism
over sequential ``Path.iterdir`` on a network filesystem.
``rebuild_instantiate`` sources ``file_ext`` from the already-loaded
parquet (every classified file comes from the parquet) and parallel-reads
``assignments.json`` via ``asyncio.Semaphore(128) + asyncio.to_thread``.

The scans assume the artifact tree is mounted and the per-stage dirs
exist. A missing dir is not an error: the pipeline has no ``pipefail``,
so the failing ``ls`` goes unnoticed and the scan returns an empty set.
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import random
import subprocess
from collections import defaultdict, deque
from pathlib import Path

import polars as pl

from .config import (
    CLASSIFY_SUBDIR as _CLASSIFY,
    CoordinatorConfig,
    DUMP_SUBDIR as _DUMP,
    INSTANTIATE_SUBDIR as _INSTANTIATE,
    ROLLOUT_SUBDIR as _ROLLOUT,
)
from .state import StageState

_ASSIGNMENTS_CONCURRENCY = 128


def walk_task_hashes(base_dir: Path, stage: str) -> set[str]:
    """Return all ``task_<hash>`` hashes under ``base_dir/<stage>/<shard>/``.

    Uses ``xargs -P 32 find`` so scan cost is ~14s for ~1M tasks on a
    network filesystem. Returns a set so downstream set algebra
    (``dump - classify``, ``classify & dump``) is a one-liner.

    Used only by ``rebuild_rollout``; ``rebuild_{download,classify,instantiate}``
    route through the marker-aware ``walk_validated_*`` helpers below so
    partial / broken task dirs are correctly excluded from "done" sets.
    """
    root = base_dir / stage
    cmd = (
        f"ls {root} | xargs -P 32 -I{{}} "
        f"find {root}/{{}} -maxdepth 1 -type d -name 'task_*' -printf '%f\\n'"
    )
    result = subprocess.run(
        ["bash", "-c", cmd], check=True, capture_output=True, text=True
    )
    return {
        line[len("task_") :]
        for line in result.stdout.splitlines()
        if line.startswith("task_")
    }


def _walk_marker_hashes(base_dir: Path, stage_subdir: str, marker_name: str) -> set[str]:
    """Return all task_<hash> hashes whose dir contains ``marker_name``.

    Mirrors ``walk_task_hashes``'s xargs -P 32 pattern. ``marker_name`` is
    a literal filename (e.g. ``.done``, ``.no_file``, ``.done_classify``,
    ``assignments.json``).
    """
    root = base_dir / stage_subdir
    cmd = (
        f"ls {root} | xargs -P 32 -I{{}} "
        f"find {root}/{{}} -mindepth 2 -maxdepth 2 -type f "
        f"-name {marker_name!r} -printf '%h\\n'"
    )
    result = subprocess.run(
        ["bash", "-c", cmd], check=True, capture_output=True, text=True
    )
    out: set[str] = set()
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        # %h prints the parent directory: .../<shard>/task_<hash>
        name = Path(line).name
        if name.startswith("task_"):
            out.add(name[len("task_"):])
    return out


def _walk_dirs_with_real_file(base_dir: Path, stage_subdir: str) -> set[str]:
    """Return all task_<hash> hashes whose dir contains at least one
    file that is NOT one of the known metadata files.

    Used to distinguish dump dirs with the actual downloaded source file
    from dump dirs with only the metadata triple
    (success-claimed-but-no-file, empty ``.done`` dirs left by earlier runs,
    classify-side outputs that happen to be in the dump tree, etc.).
    """
    root = base_dir / stage_subdir
    cmd = (
        f"ls {root} | xargs -P 32 -I{{}} "
        f"find {root}/{{}} -mindepth 2 -maxdepth 2 -type f "
        f"! -name 'task.json' "
        f"! -name 'prompt.md' "
        f"! -name '.done' "
        f"! -name '.no_file' "
        f"! -name '.done_classify' "
        f"! -name 'assignments.json' "
        f"! -name 'annotation.md' "
        f"-printf '%h\\n'"
    )
    result = subprocess.run(
        ["bash", "-c", cmd], check=True, capture_output=True, text=True
    )
    out: set[str] = set()
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        name = Path(line).name
        if name.startswith("task_"):
            out.add(name[len("task_"):])
    return out


def walk_validated_dump_hashes(base_dir: Path) -> tuple[set[str], set[str]]:
    """Validate dump-side state. Returns ``(all_done, real_file)``.

    - ``all_done``: hashes whose dump dir is in a terminal state — either
      a real download (``.done`` AND at least one non-metadata file) OR
      an intentional skip (``.no_file``). Excluded from ``rebuild_download``'s
      eligible set.
    - ``real_file``: subset of ``all_done`` where the source file is
      actually present (``.done`` AND non-metadata file). This is what
      ``rebuild_classify`` and ``rebuild_instantiate`` accept as their
      source set; ``.no_file`` dump tasks are NOT downstream-eligible
      (no source to classify or instantiate).

    Stale dirs with only ``.done`` (empty, no file) and no ``.no_file``
    fall into NEITHER set — they're treated as broken and re-eligible for
    download. The next attempt writes ``.no_file`` (or succeeds with a real
    file), so the dir self-heals over one full re-attempt cycle.
    """
    done_marker = _walk_marker_hashes(base_dir, _DUMP, ".done")
    nofile_marker = _walk_marker_hashes(base_dir, _DUMP, ".no_file")
    real_file_set = _walk_dirs_with_real_file(base_dir, _DUMP)

    real_file = done_marker & real_file_set
    all_done = real_file | nofile_marker
    return all_done, real_file


def walk_validated_classify_hashes(base_dir: Path) -> set[str]:
    """Validate classify-side state. Returns hashes whose classify dir
    is in a terminal state — either (``assignments.json`` AND
    ``annotation.md``) OR ``.no_file``.

    ``.done_classify`` is not required: the worker uses it only as a
    local agent-completion gate and does not push it to the artifact tree — the
    actual artifacts on disk (``assignments.json`` + ``annotation.md``)
    are the rebuild signal.

    Race-safety: ``push_classify`` writes ``assignments.json`` first
    and ``annotation.md`` last, so any rebuild scan that races a
    partial push either sees neither file (push hasn't finished
    assignments.json) or both (push complete). The conjunction here is
    therefore atomic w.r.t. partial pushes.

    Schema validity of ``assignments.json`` and ``template_id`` validity
    are NOT re-checked at rebuild time (they're checked by the worker
    validator). A classify dir with both files present but a malformed
    ``assignments.json`` is treated as terminal here; the next pipeline
    that consumes assignments (rebuild_instantiate) handles its own
    malformed-JSON fallback (silent skip — see ``_read_assignments``).
    """
    assignments_present = _walk_marker_hashes(base_dir, _CLASSIFY, "assignments.json")
    annotation_present = _walk_marker_hashes(base_dir, _CLASSIFY, "annotation.md")
    nofile_marker = _walk_marker_hashes(base_dir, _CLASSIFY, ".no_file")

    success_hashes = assignments_present & annotation_present
    return success_hashes | nofile_marker


def _row_task_hash(raw_url: str) -> str:
    return hashlib.sha256(raw_url.encode()).hexdigest()[:20]


def instantiate_hash_for(template_id: str, classify_task_hash: str) -> str:
    """Hash convention for instantiate (and rollout) task dirs.

    ``sha256(template_id + ":" + classify_task_hash).hexdigest()[:20]``.
    Twenty hex chars matches the existing ``task_hash`` width across the
    other two stages — directory naming stays uniform.
    """
    return hashlib.sha256(
        f"{template_id}:{classify_task_hash}".encode()
    ).hexdigest()[:20]


def rebuild_download(cfg: CoordinatorConfig, parquet: pl.DataFrame) -> StageState:
    """Rebuild the ``download`` stage's eligible set.

    ``eligible = {idx | hash(parquet[idx]["raw_url"])[:20] not in dump_done}``

    where ``dump_done`` is the set of dump task hashes in a terminal
    state (real-file download OR intentional ``.no_file`` skip), per
    ``walk_validated_dump_hashes``.

    Stale dump dirs (empty ``.done``, no file, no ``.no_file``) are
    treated as broken and remain eligible — the next download attempt
    overwrites them.
    """
    dump_done, _ = walk_validated_dump_hashes(cfg.base_dir)
    eligible: set[int | str] = {
        idx
        for idx, raw_url in enumerate(parquet["raw_url"].to_list())
        if _row_task_hash(raw_url) not in dump_done
    }
    return StageState(eligible=eligible)


def rebuild_classify(cfg: CoordinatorConfig) -> StageState:
    """Rebuild the ``classify`` stage's eligible set.

    ``eligible = dump_with_real_file − classify_done``

    where ``dump_with_real_file`` is the subset of dump tasks where the
    source file is actually present (excludes ``.no_file`` skips —
    nothing to classify), and ``classify_done`` is the relaxed
    classify-terminal set per ``walk_validated_classify_hashes``
    (``assignments.json`` + ``annotation.md`` OR ``.no_file``).

    Stale partial classify dirs (e.g. only ``prompt.md``, or
    ``.done_classify`` without ``assignments.json``) are NOT in
    ``classify_done`` and therefore re-eligible.
    """
    _, real_file = walk_validated_dump_hashes(cfg.base_dir)
    classify_done = walk_validated_classify_hashes(cfg.base_dir)
    return StageState(eligible=real_file - classify_done)


async def _read_assignments(
    classify_root: Path, hashes: list[str]
) -> list[tuple[str, list[dict]]]:
    sem = asyncio.Semaphore(_ASSIGNMENTS_CONCURRENCY)

    async def read_one(h: str) -> tuple[str, list[dict]]:
        # A classify task dir can exist without assignments.json when the
        # worker created the dir but was killed before writing the payload
        # — such dirs are skipped silently.
        path = classify_root / h[:3] / f"task_{h}" / "assignments.json"
        async with sem:
            try:
                data = await asyncio.to_thread(lambda: json.loads(path.read_text()))
            except FileNotFoundError:
                return h, []
        return h, data.get("assignments", [])

    return await asyncio.gather(*(read_one(h) for h in hashes))


def rebuild_instantiate(
    cfg: CoordinatorConfig, parquet: pl.DataFrame
) -> StageState:
    """Rebuild the ``instantiate`` queue with greedy marginal balancing.

    ``file_ext`` comes from the parquet (every classified file comes from
    the parquet, and its ``file_ext`` matches the dump's ``task.json``).
    ``assignments.json`` stays the only filesystem read, parallelized via
    ``asyncio.to_thread`` with a 128-slot semaphore. Intersecting
    ``classify & dump`` drops the handful of classify tasks whose dump
    subtree is absent.

    Returns a ``StageState`` whose ``eligible`` is a ``deque`` of
    ``(file_ext, template_id, classify_task_hash)`` tuples ordered by the
    greedy marginal balancer (``_greedy_marginal_balance``).
    """
    _, dump_real_file = walk_validated_dump_hashes(cfg.base_dir)
    classify = walk_validated_classify_hashes(cfg.base_dir)
    # Intersect on the dump side with real-file presence so instantiate
    # never tries to instantiate a task whose source file was skipped
    # (.no_file). Tasks where classify wrote .no_file end up in
    # ``classify`` but produce no items downstream because their dirs
    # have no assignments.json (see _read_assignments).
    eligible_hashes = sorted(classify & dump_real_file)

    ext_by_hash = {
        _row_task_hash(url): ext
        for url, ext in zip(
            parquet["raw_url"].to_list(), parquet["file_ext"].to_list()
        )
    }

    pairs = asyncio.run(
        _read_assignments(cfg.base_dir / _CLASSIFY, eligible_hashes)
    )
    items: list[tuple[str, str, str]] = [
        (ext_by_hash[h], entry["template_id"], h)
        for h, assignments in pairs
        for entry in assignments
        if entry.get("template_id")
    ]
    return StageState(eligible=_greedy_marginal_balance(items))


def _greedy_marginal_balance(
    items: list[tuple[str, str, str]],
) -> deque[tuple[str, str, str]]:
    """Greedy marginal balancing on ``(template_id, file_ext)``.

    Each bucket is shuffled with plain ``random.shuffle`` (no per-bucket
    reproducible seed).

    The output queue interleaves work so prefix marginals on both
    ``template_id`` and ``file_ext`` stay as uniform as possible; once a
    cell drains, weight shifts to remaining cells.
    """
    buckets: dict[tuple[str, str], list[tuple[str, str, str]]] = defaultdict(list)
    for item in items:
        file_ext, template_id, _ = item
        buckets[(template_id, file_ext)].append(item)

    for bucket in buckets.values():
        random.shuffle(bucket)

    seen_t: dict[str, int] = defaultdict(int)
    seen_e: dict[str, int] = defaultdict(int)
    queue: deque[tuple[str, str, str]] = deque()

    while True:
        live = [k for k, v in buckets.items() if v]
        if not live:
            break
        # Pick the (t, e) cell whose template AND extension are most
        # under-represented; tie-break by preferring the rarer template.
        cell = min(live, key=lambda k: (seen_t[k[0]] + seen_e[k[1]], seen_t[k[0]]))
        item = buckets[cell].pop()
        queue.append(item)
        seen_t[cell[0]] += 1
        seen_e[cell[1]] += 1

    return queue


def rebuild_rollout(cfg: CoordinatorConfig) -> StageState:
    """Rebuild the ``rollout`` stage's eligible set.

    eligible = {instantiate hashes whose stage2/.done exists} − {rollout hashes}

    Rollout consumes instantiate's stage2 artifacts. The ``.done`` marker
    read here is instantiate's ``stage2/.done`` (the agent's completion
    signal for stage 2); rollout's own ``.done`` is written for downstream
    consumers and is not checked by this rebuilder.

    The ``stage2/.done`` check is a single ``stat()`` per candidate hash,
    bounded by the size of ``instantiate − rollout``. When instantiate runs
    far ahead of rollout that is a few hundred thousand stats per rebuild —
    a few seconds on a network filesystem. If it becomes a bottleneck,
    parallelize via ``asyncio.Semaphore`` as ``_read_assignments`` does.
    """
    instantiate_root = cfg.base_dir / _INSTANTIATE
    instantiate_hashes = walk_task_hashes(cfg.base_dir, _INSTANTIATE)
    rollout_hashes = walk_task_hashes(cfg.base_dir, _ROLLOUT)

    eligible: set[int | str] = set()
    for h in instantiate_hashes - rollout_hashes:
        marker = instantiate_root / h[:3] / f"task_{h}" / "stage2" / ".done"
        if marker.exists():
            eligible.add(h)

    return StageState(eligible=eligible)
