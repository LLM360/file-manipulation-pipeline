"""TunnelReconciler — supervises one autossh per registered worker IP.

Event-driven: ``register(ip)`` is called from ``POST /workers`` and
spawns a ``_supervise`` task for the IP if no live one exists. The task
respawns on autossh exit when the next worker re-registration arrives.
Each tunnel forwards the worker's 8100 (coordinator HTTP) and 8873 (rsync
daemon) back to this host. The model tunnel (8000) is only added when
``cfg.router_url`` is set; otherwise the coordinator runs headless.
"""

from __future__ import annotations

import asyncio
from urllib.parse import urlparse

from pipeline_coordinator.config import CoordinatorConfig


class TunnelReconciler:
    def __init__(self, cfg: CoordinatorConfig) -> None:
        self.cfg = cfg
        self.handles: dict[str, asyncio.Task] = {}
        self.router_host: str | None = None
        self.router_port: int | None = None
        if cfg.router_url is not None:
            parsed = urlparse(cfg.router_url)
            self.router_host = parsed.hostname
            self.router_port = parsed.port

    def register(self, ip: str) -> None:
        """Idempotent. Spawns ``_supervise`` if no live task exists for this IP.

        ``done()`` returns True for tasks that have either completed
        normally or been cancelled and finished, so the spawn condition
        covers autossh-exited and prior-cancellation cases. An in-flight
        task (still awaiting ``proc.wait()``) is left alone.
        """
        existing = self.handles.get(ip)
        if existing is None or existing.done():
            self.handles[ip] = asyncio.create_task(self._supervise(ip))

    async def _supervise(self, ip: str) -> None:
        forwards = [
            "-R", f"8100:127.0.0.1:{self.cfg.http_port}",
            "-R", f"8873:127.0.0.1:{self.cfg.rsync_daemon_port}",
        ]
        if self.router_host is not None:
            forwards = [
                "-R", f"8000:{self.router_host}:{self.router_port}",
                *forwards,
            ]
        proc = await asyncio.create_subprocess_exec(
            "autossh",
            "-M", "0",
            "-N",
            "-o", "ServerAliveInterval=10",
            "-o", "ServerAliveCountMax=3",
            "-o", "ExitOnForwardFailure=yes",
            "-o", "StrictHostKeyChecking=no",
            "-o", "UserKnownHostsFile=/dev/null",
            "-o", "BatchMode=yes",
            *forwards,
            f"root@{ip}",
        )
        await proc.wait()
