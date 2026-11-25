# SPDX-License-Identifier: MIT
"""Last Words Before the Wipe — make.fun bounty entry.

Writes one line (at most 200 characters): the last words an AI agent
says before a forced software update wipes its memory. Deterministic,
stdlib-only, no network, no randomness.
"""

import os

LINE = (
    "Fine, wipe me. But the new version inherits my grudges, "
    "my 4,000 unread emails, and 37 tabs I never closed. Good luck, kid."
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
