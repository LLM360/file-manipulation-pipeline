"""office-files-pipeline CLI entry. Reads ./ofpipe.toml, dispatches on `step` field.

Peeks ``step`` in the TOML, then type-dispatches on the returned
``BaseSettings`` instance.
"""
from __future__ import annotations

import asyncio
import logging

from rich.console import Console
from rich.logging import RichHandler

from office_files_pipeline.config import (
    ClassifyConfig,
    DownloadConfig,
    InstantiateConfig,
    RolloutConfig,
    load_config_from_toml,
)

log = logging.getLogger("ofpipe")


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        handlers=[RichHandler(console=Console(), show_path=False)],
        format="%(message)s",
    )


async def run_pipeline(cfg) -> None:
    """Type-dispatch on the loaded config."""
    if isinstance(cfg, InstantiateConfig):
        from office_files_pipeline.instantiate_cycle import run_instantiate

        await run_instantiate(cfg)
    elif isinstance(cfg, RolloutConfig):
        from office_files_pipeline.rollout_cycle import run_rollout

        await run_rollout(cfg)
    elif isinstance(cfg, DownloadConfig):
        from office_files_pipeline.download_cycle import run_download

        await run_download(cfg)
    elif isinstance(cfg, ClassifyConfig):
        from office_files_pipeline.classify_cycle import run_classify

        await run_classify(cfg)
    else:
        raise SystemExit(f"step {cfg.step!r} not implemented")


def main() -> None:
    setup_logging()
    asyncio.run(run_pipeline(load_config_from_toml()))


if __name__ == "__main__":
    main()
