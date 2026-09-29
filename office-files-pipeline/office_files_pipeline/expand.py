"""Command-template expansion for the TOML ``cmd`` strings.

Cowbox flags live entirely inside the template and are expanded through
this helper alone — there is no secondary expansion path anywhere else.
Templates go through ``str.format``: a ``${MODEL_ID}`` left in a deployed
TOML raises ``KeyError``, so configs are rendered with ``envsubst`` first
(see docs/operations.md).
"""
from __future__ import annotations

import shlex
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ExpansionContext:
    """Placeholder values supplied to a stage's ``cmd`` template.

    Every placeholder the pipeline injects is listed here. Adding a new one
    means (1) adding a field, (2) adding a key to :meth:`as_dict`, (3)
    populating it at the call site — no runtime registry.
    """

    work_dir: Path
    stage_dir: Path
    output_dir: Path
    prompt: str

    def as_dict(self) -> dict[str, str]:
        return {
            "work_dir": shlex.quote(str(self.work_dir)),
            "stage_dir": shlex.quote(str(self.stage_dir)),
            "output_dir": shlex.quote(str(self.output_dir)),
            "prompt": shlex.quote(self.prompt),
        }


def expand_cmd(template: str, ctx: ExpansionContext) -> list[str]:
    """Expand a ``cmd`` template into an argv list.

    Values are pre-quoted via :func:`shlex.quote`; :func:`shlex.split` then
    reproduces the literal quoted values as individual argv entries.
    """
    return shlex.split(template.format(**ctx.as_dict()))
