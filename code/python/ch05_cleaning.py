"""
Chapter 5 - Cleaning, structuring, and managing data
Three small habits: reshape wide to long, read identifiers as text, and
profile missingness. The book presents these as separate fragments; they
are collected here and each runs.
"""
from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data" / "synthetic" / "incidents.csv"

# --- book code: wide to long with melt -------------------------------------
wide = pd.DataFrame({"area":["North","South"],
                     "y2019":[120,80], "y2020":[138,95]})
long = wide.melt(id_vars="area", var_name="year", value_name="robberies")
print("Tidy (long) form:")
print(long, "\n")   # one row per area-year

# --- book code: force identifier columns to text on the way in -------------
crimes = pd.read_csv(DATA, dtype={"crime_id": str})
assert crimes["crime_id"].str.len().min() > 0   # no silent loss

# --- book code: share missing per field, worst first ----------------------
missing = crimes.isna().mean().sort_values(ascending=False)
print("Percentage missing by column:")
print((missing * 100).round(1))   # percentage missing by column
