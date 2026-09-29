# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""cast.py — validate design_space.json diversity and sample a cell.

Dual mode:

    (1) CLI / subprocess (what the stage-1 agent runs inside cowbox):
            uv run cast.py --seed <seed> path/to/design_space.json
        On pass: writes <dir>/design_brief.md with YAML frontmatter that
        encodes one sampled {value, behavioral} entry per axis, then an
        empty body marked for the agent's prose. Exit 0.
        On fail: writes a per-axis diagnostic to stderr. Exit 1.

    (2) Importable (what the worker uses at resume-time validation):
            from cast import sample_cell
            cell = sample_cell(design_space_dict, seed_str)
        Returns the same dict shape the CLI writes into the frontmatter.
        Raises ValueError / DiversityDeficit on schema or threshold errors.

Threshold: product of ``len(axis.values)`` across axes where
``behavioral is True`` must clear ``BEHAVIORAL_FLOOR`` (100). Cosmetic
axes are sampled but do not count toward the floor.

The seed derivation is pinned: ``int.from_bytes(sha256(seed).digest()[:8],
'big')`` so CLI and import paths agree byte-for-byte on the sampled cell —
which is what makes the worker's resume-time re-run a meaningful
anti-fabrication check.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from functools import reduce
from operator import mul
from pathlib import Path
from typing import Any


BEHAVIORAL_FLOOR = 100
REQUIRED_FIELDS = ("values", "behavioral", "rationale")
BODY_MARKER = "<!-- agent prose: interpret the sampled brief here -->"


class DiversityDeficit(ValueError):
    """Behavioral-axes product is below ``BEHAVIORAL_FLOOR``.

    Carries the full axis map so the CLI can render the teaching diagnostic
    without re-parsing the design space. Importers that do not need the
    diagnostic can rely on the base ``ValueError`` semantics.
    """

    def __init__(self, axes: dict[str, dict], behavioral_product: int) -> None:
        self.axes = axes
        self.behavioral_product = behavioral_product
        super().__init__(
            f"behavioral-axes product {behavioral_product} < floor {BEHAVIORAL_FLOOR}"
        )


def _extract_axes(design_space: dict) -> dict[str, dict]:
    # Every top-level value that is a JSON object is treated as a candidate
    # axis and validated strictly. Non-dict top-level values (strings,
    # numbers, nulls, arrays) are freeform siblings and ignored.
    return {name: val for name, val in design_space.items() if isinstance(val, dict)}


def _validate_axes(axes: dict[str, dict]) -> list[str]:
    errors: list[str] = []
    for name, axis in axes.items():
        missing = [f for f in REQUIRED_FIELDS if f not in axis]
        if missing:
            errors.append(
                f"axis {name!r}: missing required field(s): {', '.join(missing)}"
            )
            continue
        values = axis["values"]
        if not isinstance(values, list) or not values:
            errors.append(f"axis {name!r}: 'values' must be a non-empty list")
        if not isinstance(axis["behavioral"], bool):
            errors.append(f"axis {name!r}: 'behavioral' must be true or false")
        if not isinstance(axis["rationale"], str):
            errors.append(f"axis {name!r}: 'rationale' must be a string")
    return errors


def _seed_to_int(seed: str) -> int:
    return int.from_bytes(hashlib.sha256(seed.encode()).digest()[:8], "big")


def _behavioral_product(axes: dict[str, dict]) -> int:
    return reduce(
        mul,
        (len(a["values"]) for a in axes.values() if a["behavioral"]),
        1,
    )


def sample_cell(design_space: dict, seed: str) -> dict[str, dict]:
    """Validate ``design_space`` and deterministically sample one value per axis.

    Returns ``{axis_name: {"value": ..., "behavioral": bool}}`` — the same
    dict shape the CLI renders into ``design_brief.md``'s YAML frontmatter.

    Raises:
        ValueError: top level is not a dict, no axes are present, or any
            axis fails schema validation.
        DiversityDeficit: behavioral-axes product is below the floor.
    """
    if not isinstance(design_space, dict):
        raise ValueError(
            "design_space must be a JSON object mapping axis names to axis objects"
        )
    axes = _extract_axes(design_space)
    if not axes:
        raise ValueError(
            "design_space has no axes — expected top-level objects with fields "
            f"{REQUIRED_FIELDS}"
        )
    schema_errors = _validate_axes(axes)
    if schema_errors:
        raise ValueError("schema errors:\n  " + "\n  ".join(schema_errors))

    behavioral_product = _behavioral_product(axes)
    if behavioral_product < BEHAVIORAL_FLOOR:
        raise DiversityDeficit(axes, behavioral_product)

    rng = random.Random(_seed_to_int(seed))
    cell: dict[str, dict] = {}
    for name, axis in axes.items():
        cell[name] = {
            "value": rng.choice(axis["values"]),
            "behavioral": axis["behavioral"],
        }
    return cell


def _format_deficit_diagnostic(
    axes: dict[str, dict], behavioral_product: int
) -> str:
    """Report product+floor and per-axis cardinalities with the
    ``(behavioral)`` / ``(cosmetic)`` tag visible, and end with a teaching
    hint pointing at the common failure modes.
    """
    cosmetic_axes = [(n, a) for n, a in axes.items() if not a["behavioral"]]
    name_w = max(len(n) for n in axes)
    tag_w = len("(behavioral)")

    lines = ["cast.py: validation FAILED", ""]
    lines.append(
        f"  behavioral-axes product: {behavioral_product} (floor: {BEHAVIORAL_FLOOR})"
    )
    if cosmetic_axes:
        cosmetic_product = reduce(
            mul, (len(a["values"]) for _, a in cosmetic_axes), 1
        )
        lines.append(
            f"  cosmetic-axes product:   {cosmetic_product}  (not counted)"
        )
    lines.append("")
    lines.append("  per-axis cardinalities:")
    for name, axis in axes.items():
        tag = "(behavioral)" if axis["behavioral"] else "(cosmetic)"
        card = len(axis["values"])
        nudge = (
            "   <- low; consider adding values or deeper granularity"
            if axis["behavioral"] and card < 3
            else ""
        )
        lines.append(
            f"    {name:<{name_w}} {tag:<{tag_w}} : {card} values{nudge}"
        )
    lines.append("")
    lines.append(
        "  hint: the behavioral-axes product is below the floor. Common fixes:"
    )
    lines.append("    - Add more values to an existing behavioral axis.")
    lines.append(
        "    - Add a new behavioral axis (apply the manifold's calibration"
    )
    lines.append(
        "      check: do two neighbouring values change what the runner opens,"
    )
    lines.append("      consults, or produces?).")
    lines.append(
        "    - If two of your behavioral axes collapse into the same underlying"
    )
    lines.append(
        "      distinction, merging them can reveal what is actually varying."
    )
    return "\n".join(lines)


def _yaml_scalar(value: Any) -> str:
    """Serialize a JSON scalar as a YAML scalar.

    Supports the subset present in a sampled cell: bool, int, float, None, str.
    Strings are always double-quoted with ``\\`` and ``"`` escaped — safer
    than trying to distinguish quoting-required from plain.
    """
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return repr(value)
    if isinstance(value, str):
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    raise ValueError(
        f"cannot serialize value of type {type(value).__name__!r} as a YAML scalar"
    )


def _render_brief(cell: dict[str, dict]) -> str:
    lines = ["---"]
    for name, entry in cell.items():
        lines.append(f"{name}:")
        lines.append(f"  value: {_yaml_scalar(entry['value'])}")
        lines.append(f"  behavioral: {_yaml_scalar(entry['behavioral'])}")
    lines.append("---")
    lines.append("")
    lines.append(BODY_MARKER)
    lines.append("")
    return "\n".join(lines)


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="cast.py",
        description=(
            "Validate a design_space.json and, on pass, deterministically "
            "sample one value per axis into design_brief.md."
        ),
    )
    parser.add_argument(
        "--seed",
        required=True,
        help="seed string for deterministic sampling (typically the task hash)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=(
            "directory where design_brief.md is written "
            "(default: same directory as the design_space.json argument)"
        ),
    )
    parser.add_argument(
        "design_space",
        type=Path,
        help="path to design_space.json",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    try:
        raw = args.design_space.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"cast.py: cannot read {args.design_space}: {exc}", file=sys.stderr)
        return 1
    try:
        design_space = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(
            f"cast.py: {args.design_space} is not valid JSON: {exc}",
            file=sys.stderr,
        )
        return 1

    try:
        cell = sample_cell(design_space, args.seed)
    except DiversityDeficit as exc:
        print(
            _format_deficit_diagnostic(exc.axes, exc.behavioral_product),
            file=sys.stderr,
        )
        return 1
    except ValueError as exc:
        print(f"cast.py: validation FAILED\n\n  {exc}", file=sys.stderr)
        return 1

    out_dir = (
        args.output_dir if args.output_dir is not None else args.design_space.parent
    )
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"cast.py: cannot create {out_dir}: {exc}", file=sys.stderr)
        return 1
    (out_dir / "design_brief.md").write_text(_render_brief(cell), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
