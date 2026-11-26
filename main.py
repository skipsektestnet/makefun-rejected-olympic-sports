"""Rejected Olympic Sports: writes the rejected sport to /output/entry.txt.

Why this line: a full fake sport with its own judging criteria, and the
rejection reason is the joke itself: too relatable to be a sport.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'Competitive napping: athletes sleep eight hours while judges score drool, snoring, and how dramatically they wake up. Rejected for being too relatable.'

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote entry.txt", len(ENTRY), "chars")


if __name__ == "__main__":
    main()
