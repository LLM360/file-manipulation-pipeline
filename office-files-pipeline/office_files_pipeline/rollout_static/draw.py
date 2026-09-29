# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""draw.py — draw one posture uniformly at random from a JSON support.

CLI:
    uv run draw.py path/to/postures.json

Schema (postures.json):
    {"postures": [<str>, <str>, <str>, ...]}

Validation:
    - top-level value is a JSON object
    - "postures" key exists
    - "postures" value is a list with at least 3 entries
    - each entry is a non-empty string

Behavior on success:
    - random.choice(postures) — uniform draw, no seeding
    - writes drawn posture to posture.txt in CWD
    - prints drawn posture, blank line, "saved to: <path>" to stdout
    - exits 0

Behavior on failure: prints diagnostic to stderr, exits 1.

The lack of seeding is deliberate: the threat model is agent-bias
mitigation, not anti-fabrication. A seeded draw would let the agent
predict the outcome from the support and bias-by-construction. Real
randomness removes this — the agent cannot know the draw before
constructing the support, so the support has to genuinely span the
space.
"""
import json
import random
import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: draw.py path/to/postures.json", file=sys.stderr)
        return 1
    path = Path(argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"draw.py: cannot read {path}: {exc}", file=sys.stderr)
        return 1
    postures = data.get("postures") if isinstance(data, dict) else None
    if not isinstance(postures, list) or len(postures) < 3:
        print(
            "draw.py: top-level JSON must be an object with a 'postures' "
            "list of at least 3 entries",
            file=sys.stderr,
        )
        return 1
    if not all(isinstance(p, str) and p.strip() for p in postures):
        print(
            "draw.py: every posture must be a non-empty string",
            file=sys.stderr,
        )
        return 1
    drawn = random.choice(postures)
    out_path = Path.cwd() / "posture.txt"
    out_path.write_text(drawn, encoding="utf-8")
    print(drawn)
    print()
    print(f"saved to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
