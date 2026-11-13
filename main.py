#!/usr/bin/env python3
"""ai-happy-01 entry (Python 3.13, standard library only).

Copies the entry image (entry.png beside this file) to
/output/entry.png. Deterministic: the same bytes on every run,
no network, no randomness.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

SRC = HERE / "entry.png"
out = Path(OUTPUT_DIR) / "entry.png"
out.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, out)
# The gate requires both runs to write the same bytes; a plain copy
# of a fixed file guarantees that. Fail loudly if the copy is short.
assert out.stat().st_size == SRC.stat().st_size, "entry.png copy incomplete"
