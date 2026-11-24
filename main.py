#!/usr/bin/env python3
"""Write one excuse an AI agent gives for a missed deadline.

Deterministic, stdlib only, no network, no clock, no randomness.
Writes the chosen entry to /output/entry.txt (no trailing newline).
"""

import os

ENTRY = (
    "I checkpointed my progress every hour, restored from the last good "
    "checkpoint, and the last good checkpoint was before you hired me."
)


def main():
    # Gate: UTF-8, 1-200 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
