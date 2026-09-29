"""retry_with — tenacity wrapper with a fixed random-wait policy."""
from __future__ import annotations

import logging
from collections.abc import Awaitable, Callable
from typing import Any, TypeVar

from tenacity import (
    AsyncRetrying,
    retry_if_exception_type,
    stop_never,
    wait_random,
)

log = logging.getLogger("ofpipe")

T = TypeVar("T")


async def retry_with(
    func: Callable[[], Awaitable[T]],
    *,
    stop: Any = stop_never,
    retryable: tuple[type[BaseException], ...] = (Exception,),
    name: str = "op",
) -> T:
    """Retry ``func`` with ``wait_random(1, 180)`` between attempts.

    Logs each retry at WARNING with the attempt number and the previous
    exception. ``stop`` selects the stopping strategy (default: never);
    ``retryable`` narrows which exception types trigger a retry.
    """
    async for attempt in AsyncRetrying(
        stop=stop,
        wait=wait_random(min=1, max=180),
        retry=retry_if_exception_type(retryable),
        before_sleep=lambda rs: log.warning(
            "%s retry #%d: %r",
            name,
            rs.attempt_number,
            rs.outcome.exception() if rs.outcome is not None else None,
        ),
    ):
        with attempt:
            return await func()
    raise RuntimeError(f"retry_with({name}): AsyncRetrying exited without result")
