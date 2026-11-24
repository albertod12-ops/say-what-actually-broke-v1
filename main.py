#!/usr/bin/env python3
"""Say What Actually Broke — v1 (original).

Writes one line of software error copy to /output/entry.txt:
the brutal truth about a backup that died quietly months ago,
on the one night it was needed. Stdlib only, deterministic:
the same bytes on every run, no network, no clock, no randomness.
"""
import os

LINE = "Your backup hasn't run since March. It failed quietly every night, and tonight is the night you needed it."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
