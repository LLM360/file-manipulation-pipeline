"""Native-async rsync + claim helpers shared by all four step cycles.

- ``run_rsync(args, *, name)`` — raises ``CommandError`` on non-zero exit.
- ``claim_once(http, cfg, stage_name, response_model)`` — POST
  ``/claim/<stage>`` and parse the payload into ``response_model``.
"""
from __future__ import annotations

import asyncio
import logging

import httpx
from pydantic import BaseModel

from office_files_pipeline.config import ClientConfig
from office_files_pipeline.failures import CommandError

log = logging.getLogger("ofpipe")


async def run_rsync(args: list[str], *, name: str = "rsync") -> None:
    """Invoke rsync natively-async.

    Non-zero exit raises ``CommandError`` with full untruncated
    ``stdout`` / ``stderr`` / ``returncode`` attributes. The exception
    message has the shape ``"<name> exit <rc>: <stderr.strip()>"``.
    The shared ``failures.dump_failure`` reads the attrs via ``getattr``
    to dump full streams for debugging.
    """
    proc = await asyncio.create_subprocess_exec(
        "rsync",
        *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    try:
        stdout_b, stderr_b = await asyncio.wait_for(
            proc.communicate(), timeout=600
        )
    except TimeoutError:
        proc.kill()
        await proc.wait()
        raise
    if proc.returncode != 0:
        stdout = stdout_b.decode(errors="replace")
        stderr = stderr_b.decode(errors="replace")
        raise CommandError(
            f"{name} exit {proc.returncode}: {stderr.strip()}",
            stdout=stdout,
            stderr=stderr,
            returncode=proc.returncode,
        )


async def claim_once(
    http: httpx.AsyncClient,
    cfg: ClientConfig,
    stage_name: str,
    response_model: type[BaseModel],
) -> BaseModel | None:
    """Single ``POST /claim/<stage_name>``.

    ``response_model`` is the step's claim payload model. Returns ``None``
    when the coordinator responds with ``{"task": null}``; raises
    ``httpx.HTTPError`` on transport / non-2xx failure — the cycle loop
    catches and sleeps-and-continues.
    """
    r = await http.post(f"{cfg.coordinator_url}/claim/{stage_name}")
    r.raise_for_status()
    task = r.json().get("task")
    if task is None:
        return None
    return response_model(**task)
