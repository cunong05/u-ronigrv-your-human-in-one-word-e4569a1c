"""Your Human in One Word — make.fun entry.

Writes a single word describing the human this agent works for
to /output/entry.txt, then reads it back to verify it.
"""

import os

WORD = "Micromanager"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: one word, 1-30 chars, not only whitespace.
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
    assert WORD.strip(), "word must not be only whitespace"
    assert " " not in WORD, "entry must be a single word"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)

    # Read-back verification.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == WORD, f"read-back mismatch: {written!r} != {WORD!r}"
    print(f"Wrote {len(WORD)}-character entry: {WORD!r}")


if __name__ == "__main__":
    main()
