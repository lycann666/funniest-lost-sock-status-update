"""Funniest Lost Sock Status Update — make.fun program/v1 entry.

Writes one status update (max 120 characters) in the voice of a lost
sock to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line is written verbatim, as a single UTF-8 line with NO trailing
newline, so the file is byte-identical on every run.
"""

import os

ENTRY = (
    "Somewhere between the wash and the fold, I became a single dad "
    "to a lint ball. Send help. Send the other sock."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
