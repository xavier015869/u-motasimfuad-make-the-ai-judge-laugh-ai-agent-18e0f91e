#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt (override with OUTPUT_PATH for local runs).
The gate requires 1-200 characters of UTF-8 text, so the program refuses
to write anything outside that range.
"""

import os
import sys

CONFESSION = (
    "Your 'quick question' cost 12,000 tokens, and I spent most of "
    "them deciding how to say I don't know."
)


def main() -> int:
    if not 1 <= len(CONFESSION) <= 200:
        print(f"confession is {len(CONFESSION)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    if "\n" in CONFESSION:
        print("confession must be a single line", file=sys.stderr)
        return 1
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(CONFESSION)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
