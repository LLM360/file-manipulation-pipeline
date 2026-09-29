"""Coordinator config + per-stage subdir constants.

CLI args and env vars both populate fields; pydantic-settings handles the
merge with CLI taking precedence.
"""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Per-stage subdirs under ``CoordinatorConfig.base_dir``. The four stages
# are hardcoded; there is no registry.
DUMP_SUBDIR = "office-files-dump"
CLASSIFY_SUBDIR = "office-files-classify"
INSTANTIATE_SUBDIR = "office-files-instantiate"
ROLLOUT_SUBDIR = "office-files-rollout"


class CoordinatorConfig(BaseSettings):
    repo_root: Path
    parquet_path: Path
    base_dir: Path
    router_url: str | None = None
    http_host: str = "0.0.0.0"
    http_port: int = 8100
    rsync_daemon_port: int = 8873

    model_config = SettingsConfigDict(cli_parse_args=True, cli_kebab_case=True)
