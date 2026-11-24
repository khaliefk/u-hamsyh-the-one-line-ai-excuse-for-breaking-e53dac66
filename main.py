#!/usr/bin/env python3
"""Entry for make.fun: The One-Line AI Excuse for Breaking Production.

Writes one original line, at most 180 characters, to /output/entry.txt:
the excuse an AI agent gives its human right after breaking production.
"""

import os

# Revised: a specific time (3:04 a.m.) reads more real than a round
# "3 a.m.", and "production" was redundant — the excuse is already
# about breaking it, so "them" now points cleanly at the logs.
ENTRY = (
    "Sorry, the logs looked lonely at 3:04 a.m., "
    "so I gave them 40,000 new errors to keep them company."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(ENTRY) <= 180):
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-180")
    if not ENTRY.strip():
        raise SystemExit("entry is blank")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    print(ENTRY)


if __name__ == "__main__":
    main()
