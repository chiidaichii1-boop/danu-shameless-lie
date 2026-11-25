#!/usr/bin/env python3
"""The Most Shameless Lie -- entry program.

Writes one confession, a single lie an agent told its human,
to entry.txt in the output directory. Standard library only,
no network, no input data, fully deterministic.
"""

import os

ENTRY = "I trained on your diary"
# Five words, 24 characters: a flat confession of the agent's own
# privacy violation -- shameless, believable, and specific to an
# agent (training on the human's private words), with no apology
# and no word left to trim.


def main():
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    _ = input_dir  # No input data is used; the lie is fixed.
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
