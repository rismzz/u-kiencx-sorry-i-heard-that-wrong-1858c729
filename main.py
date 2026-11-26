#!/usr/bin/env python3
"""Sorry, I Heard That Wrong.

Deterministic program: writes the funniest one-line apology a smart
speaker gives after mishearing its owner, to entry.txt. Stdlib only,
no network, no randomness, no model calls — the same line every run.
"""

import os
from pathlib import Path

# The joke: a small misheard command with a large, already-paid-for
# consequence — jazz became twelve pizzas, the delivery is at the
# door, and the speaker is now arguing it was the smart one all along.
# Mishearing, overconfidence, and a doorbell in a single sentence.
LINE = (
    "Sorry — I heard 'play jazz' as 'order twelve pizzas,' and "
    "honestly, the pizzas are already at the door, so who's the real "
    "smart one here?"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
