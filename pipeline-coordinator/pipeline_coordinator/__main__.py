"""Entry point for ``python -m pipeline_coordinator``.

The rsync daemon runs as an ``asyncio`` subprocess owned by the app's
lifespan. Workers register over HTTP (``POST /workers``); there is no
polling task.

Wiring, in order:

1. Load ``CoordinatorConfig`` (CLI args + env vars) via pydantic-settings.
2. Read the parquet once (shared with the ``/claim/download`` hot path and
   ``rebuild_instantiate``).
3. Synchronously rebuild all four stages — blocks until the filesystem
   scans finish, so uvicorn's port does not open until ``eligible``
   containers are populated.
4. Bundle parquet + reconciler + stage states into ``AppRuntime`` and
   hand to ``create_app``.
5. Install a lifespan that spawns the rsync daemon and tears down both
   rsync and any registered autossh tasks at shutdown.
6. Run uvicorn on ``http_host:http_port``.
"""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager

import polars as pl
import uvicorn

from .api import create_app
from .config import CoordinatorConfig
from .rebuild import rebuild_classify, rebuild_download, rebuild_instantiate, rebuild_rollout
from .reconciler import TunnelReconciler
from .state import AppRuntime


def _generate_rsyncd_conf(cfg: CoordinatorConfig) -> str:
    """Body of the rsyncd.conf that serves ``base_dir`` as the ``artifacts`` module."""
    return (
        "use chroot = no\n"
        "max connections = 0\n"
        f"log file = {cfg.repo_root}/logs/rsyncd.log\n"
        f"lock file = {cfg.repo_root}/logs/rsyncd.lock\n"
        "\n"
        "[artifacts]\n"
        f"    path = {cfg.base_dir}\n"
        "    read only = false\n"
        "    list = no\n"
    )


def main() -> None:
    cfg = CoordinatorConfig()
    parquet = pl.read_parquet(cfg.parquet_path)
    reconciler = TunnelReconciler(cfg)
    runtime = AppRuntime(
        parquet=parquet,
        stages={
            "download": rebuild_download(cfg, parquet),
            "classify": rebuild_classify(cfg),
            "instantiate": rebuild_instantiate(cfg, parquet),
            "rollout": rebuild_rollout(cfg),
        },
        reconciler=reconciler,
    )
    app = create_app(cfg, runtime)

    @asynccontextmanager
    async def lifespan(_app):
        rsyncd_conf = cfg.repo_root / ".state" / "rsyncd.conf"
        rsyncd_conf.parent.mkdir(parents=True, exist_ok=True)
        rsyncd_conf.write_text(_generate_rsyncd_conf(cfg))

        rsync_proc = await asyncio.create_subprocess_exec(
            "rsync", "--daemon", "--no-detach",
            f"--config={rsyncd_conf}",
            f"--port={cfg.rsync_daemon_port}",
            "--address=127.0.0.1",
        )
        try:
            yield
        finally:
            rsync_proc.terminate()
            try:
                await asyncio.wait_for(rsync_proc.wait(), timeout=5.0)
            except asyncio.TimeoutError:
                rsync_proc.kill()
                await rsync_proc.wait()
            for task in reconciler.handles.values():
                task.cancel()

    app.router.lifespan_context = lifespan
    uvicorn.run(app, host=cfg.http_host, port=cfg.http_port, log_level="info")


if __name__ == "__main__":
    main()
