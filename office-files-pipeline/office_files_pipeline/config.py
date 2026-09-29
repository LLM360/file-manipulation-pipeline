"""Pydantic-settings configuration.

One ``BaseSettings`` subclass per step. The TOML's top-level ``step``
field selects which class loads at dispatch time (``load_config_from_toml``).
"""
from __future__ import annotations

import logging
import tomllib
from importlib.resources import files
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_settings.sources.providers.toml import TomlConfigSettingsSource

log = logging.getLogger("ofpipe")


class StepConfig(BaseModel):
    """Per-stage config.

    ``cmd`` template placeholders: ``{work_dir}``, ``{stage_dir}``,
    ``{output_dir}``, ``{prompt}``. The cowbox sandbox invocation lives
    inside the template, and env vars flow through its ``env VAR=val cmd``
    shell prefix.
    """

    name: str = Field(description="Stage name (e.g. 'stage1', 'stage2').")
    cmd: str = Field(description="Command template — expanded by expand_cmd().")
    prompt_file: Path | None = Field(
        default=None,
        description=(
            "Optional path to the stage prompt template, relative to the "
            "office_files_pipeline package. Rollout leaves it unset: it "
            "pulls each task's prompt.md from the instantiate output."
        ),
    )
    timeout: int = Field(default=2400, description="Per-stage timeout (seconds).")

    @field_validator("prompt_file", mode="after")
    @classmethod
    def resolve_against_package(cls, v: Path | None) -> Path | None:
        """Resolve relative prompt_file paths against the office_files_pipeline
        package install location. Absolute paths and None pass through
        unchanged.
        """
        if v is None or v.is_absolute():
            return v
        return Path(str(files("office_files_pipeline").joinpath(str(v))))


class ClientConfig(BaseModel):
    """VM-local coordinator + rsync daemon endpoints."""

    coordinator_url: str = Field(default="http://127.0.0.1:8100")
    rsync_host: str = Field(default="127.0.0.1")
    rsync_port: int = Field(default=8873)


class InstantiateConfig(BaseSettings):
    """Instantiate step, loaded from ``ofpipe.toml``."""

    step: Literal["instantiate"] = "instantiate"
    concurrency: int = Field(default=30, description="Per-worker coroutines.")
    output_dir: Path = Field(description="Local working directory (cleaned on startup).")
    max_retries: int = Field(
        default=10,
        description="Top-level per-attempt cap covering one full cycle.",
    )
    diversity_threshold: int = Field(
        default=100,
        description=(
            "Behavioral-axes product floor, available to the stage prompts "
            "as {diversity_threshold}; cast.py enforces BEHAVIORAL_FLOOR."
        ),
    )
    failure_log_path: Path = Field(
        default=Path("/root/pipeline-failures.jsonl"),
        description=(
            "Shared failure ledger across all steps "
            "(disambiguated per-record by the 'step' field)."
        ),
    )
    client: ClientConfig = Field(default_factory=ClientConfig)
    stages: list[StepConfig] = Field(
        description="Ordered stages; length 2 for instantiate."
    )

    model_config = SettingsConfigDict(
        toml_file="ofpipe.toml",
        env_prefix="OFPIPE_",
        env_nested_delimiter="__",
    )

    @classmethod
    def settings_customise_sources(cls, settings_cls, **kwargs):
        return (
            kwargs["init_settings"],
            kwargs["env_settings"],
            TomlConfigSettingsSource(settings_cls),
        )


class RolloutConfig(BaseSettings):
    """Rollout step, loaded from ``ofpipe.toml``.

    Two-stage cycle:
    - stages[0] = ``rollout_stage1`` (modify agent — edits the rendered system prompt)
    - stages[1] = ``rollout_stage2`` (the actual rollout, with FORGE_SYSTEM_PROMPT_FILE)
    """

    step: Literal["rollout"] = "rollout"
    concurrency: int = Field(
        default=100,
        description="Per-worker async coroutines.",
    )
    output_dir: Path = Field(
        description="Local working dir, e.g. /root/rollout-output."
    )
    max_retries: int = Field(
        default=3,
        description="Per-task attempts; after the last one the task is logged as exhausted.",
    )
    failure_log_path: Path = Field(
        default=Path("/root/pipeline-failures.jsonl"),
        description=(
            "Shared failure ledger across all steps "
            "(disambiguated per-record by the 'step' field)."
        ),
    )
    client: ClientConfig = Field(default_factory=ClientConfig)
    skip_stage1_prob: float = Field(
        default=0.05,
        ge=0.0, le=1.0,
        description=(
            "Probability of skipping stage1 (modify agent) and using the "
            "rendered original system prompt verbatim. Provides a baseline "
            "arm in the corpus and stress-tests the no-modify path of the "
            "byte-equality gate. 0.0 disables; 1.0 sends every task "
            "through the original prompt."
        ),
    )
    render_cmd: str = Field(
        description=(
            "Command template for the prepare-time `forge prompt render` "
            "subprocess. Same expand pattern as stages.cmd: {work_dir}, "
            "{output_dir}, {prompt}. The prompt placeholder is unused by "
            "render but is part of the expansion contract."
        ),
    )
    stages: list[StepConfig] = Field(
        description=(
            "Two-element list — [rollout_stage1, rollout_stage2]. "
            "Length is not schema-constrained; a misconfigured TOML surfaces "
            "as IndexError on the first task in the failure log."
        ),
    )

    model_config = SettingsConfigDict(
        toml_file="ofpipe.toml",
        env_prefix="OFPIPE_",
        env_nested_delimiter="__",
    )

    @classmethod
    def settings_customise_sources(cls, settings_cls, **kwargs):
        return (
            kwargs["init_settings"],
            kwargs["env_settings"],
            TomlConfigSettingsSource(settings_cls),
        )


class DownloadConfig(BaseSettings):
    """Download step, loaded from ``ofpipe.toml``."""

    step: Literal["download"] = "download"
    concurrency: int = Field(default=175, description="Per-worker coroutines.")
    output_dir: Path = Field(description="Local working directory (cleaned on startup).")
    max_retries: int = Field(
        default=10,
        description="Top-level per-attempt cap covering one full cycle.",
    )
    failure_log_path: Path = Field(
        default=Path("/root/pipeline-failures.jsonl"),
        description=(
            "Shared failure ledger across all steps "
            "(disambiguated per-record by the 'step' field)."
        ),
    )
    client: ClientConfig = Field(default_factory=ClientConfig)
    stages: list[StepConfig] = Field(
        description="Ordered stages; length 1 for download.",
    )

    model_config = SettingsConfigDict(
        toml_file="ofpipe.toml",
        env_prefix="OFPIPE_",
        env_nested_delimiter="__",
    )

    @classmethod
    def settings_customise_sources(cls, settings_cls, **kwargs):
        return (
            kwargs["init_settings"],
            kwargs["env_settings"],
            TomlConfigSettingsSource(settings_cls),
        )


class ClassifyConfig(BaseSettings):
    """Classify step, loaded from ``ofpipe.toml``."""

    step: Literal["classify"] = "classify"
    concurrency: int = Field(default=175, description="Per-worker coroutines.")
    output_dir: Path = Field(description="Local working directory (cleaned on startup).")
    max_retries: int = Field(
        default=10,
        description="Top-level per-attempt cap covering one full cycle.",
    )
    failure_log_path: Path = Field(
        default=Path("/root/pipeline-failures.jsonl"),
        description=(
            "Shared failure ledger across all steps "
            "(disambiguated per-record by the 'step' field)."
        ),
    )
    client: ClientConfig = Field(default_factory=ClientConfig)
    stages: list[StepConfig] = Field(
        description="Ordered stages; length 1 for classify.",
    )

    model_config = SettingsConfigDict(
        toml_file="ofpipe.toml",
        env_prefix="OFPIPE_",
        env_nested_delimiter="__",
    )

    @classmethod
    def settings_customise_sources(cls, settings_cls, **kwargs):
        return (
            kwargs["init_settings"],
            kwargs["env_settings"],
            TomlConfigSettingsSource(settings_cls),
        )


_STEP_CLASSES: dict[str, type[BaseSettings]] = {
    "download": DownloadConfig,
    "classify": ClassifyConfig,
    "instantiate": InstantiateConfig,
    "rollout": RolloutConfig,
}


def load_config_from_toml() -> BaseSettings:
    """Read ``./ofpipe.toml``, peek the ``step`` field, return the matching config.

    The chosen class is then re-loaded via TomlConfigSettingsSource (its
    ``settings_customise_sources``), preserving env-var override behavior
    (``OFPIPE_*``). The peek is a plain ``tomllib.load`` so ``step`` is
    available before pydantic-settings constructs the BaseSettings — a
    discriminated union under one BaseSettings would force every TOML to
    nest under ``[config.<step>]``.
    """
    with Path("ofpipe.toml").open("rb") as fh:
        raw = tomllib.load(fh)
    step = raw.get("step")
    cls = _STEP_CLASSES.get(step)
    if cls is None:
        raise SystemExit(
            f"ofpipe.toml: missing or unknown 'step': {step!r}; "
            f"expected one of {sorted(_STEP_CLASSES)}"
        )
    return cls()
