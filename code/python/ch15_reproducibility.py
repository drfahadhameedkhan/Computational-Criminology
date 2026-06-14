"""
Chapter 15 - Reproducibility and open science
The three habits that make an analysis rebuildable: a fixed seed, a clean
raw-to-outputs flow, and a recorded environment. Self-contained.
"""
# --- book code (Chapter 15) ------------------------------------------------
# Python: the three habits
import numpy as np
np.random.seed(42)                  # 1. repeatable randomness
from pathlib import Path
RAW = Path("data/raw"); OUT = Path("outputs")   # 2. read raw, write outputs
# 3. record the environment, once, at the shell:
#    pip freeze > requirements.txt

print("seed fixed; reading from", RAW, "writing to", OUT)
print("a second run with the same seed reproduces every figure to the digit")
