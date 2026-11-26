#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry.

Writes a single line, in English, to /output/entry.txt:
the one line the writer would send back to his younger self.
"""

import os

ENTRY = (
    "Kid, your left hand breaks at twenty-eight and never heals right — "
    "stop waiting for it to, and teach the other one "
    "everything it knows."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
