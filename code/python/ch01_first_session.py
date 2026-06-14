"""
Chapter 1 - The shape of computational criminology
Your first computational session: load a dataset and look at it.

Run from the repository root:
    python data/synthetic/make_synthetic_data.py   # once, to create the data
    python code/python/ch01_first_session.py
"""
from pathlib import Path

# --- setup: point at the synthetic incidents file shipped with the repo ---
DATA = Path(__file__).resolve().parents[2] / "data" / "synthetic" / "incidents.csv"

# --- book code (Chapter 1) -------------------------------------------------
import pandas as pd                  # the standard data library
crime = pd.read_csv(DATA)            # read a file into a table
print(crime.shape)                   # (rows, columns)
print(crime.describe(include='all')) # a quick description of each column
