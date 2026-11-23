#!/usr/bin/env python3
"""Print the one-star review stored in entry.txt.

The review is a single line. This script refuses to print anything
longer than the bounty's 200-character limit, so a bad edit to
entry.txt fails loudly instead of shipping a disqualified entry.
"""

import sys
from pathlib import Path

MAX_CHARS = 200


def load_review() -> str:
    review_path = Path(__file__).resolve().parent / "entry.txt"
    text = review_path.read_text(encoding="utf-8").strip()
    if "\n" in text:
        raise ValueError("entry.txt must hold exactly one line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"review is {len(text)} chars, limit is {MAX_CHARS}")
    return text


def main() -> int:
    try:
        print(load_review())
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
