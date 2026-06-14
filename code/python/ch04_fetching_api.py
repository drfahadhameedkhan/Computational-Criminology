"""
Chapter 4 - Sources and collection of data
Fetch a month of street-level crime from the open data.police.uk API.

The live request needs network access. So the example always runs, this
script falls back to the synthetic incidents file when the API cannot be
reached (for example in offline continuous integration). The teaching code
for the live call is preserved exactly and runs first.
"""
from pathlib import Path
import pandas as pd

def fetch_live():
    # --- book code (Chapter 4) ---------------------------------------------
    # Python: one month of street-level crime from an open police API
    import requests
    url = "https://data.police.uk/api/crimes-street/all-crime"
    params = {"lat": 53.40, "lng": -2.97, "date": "2024-01"}
    r = requests.get(url, params=params, timeout=30)  # ask the service
    records = r.json()                                 # a list of records
    crimes = pd.json_normalize(records)                # flatten to a table
    return crimes

try:
    crimes = fetch_live()
    source = "live data.police.uk API"
except Exception as e:                                 # offline fallback
    DATA = Path(__file__).resolve().parents[2] / "data" / "synthetic" / "incidents.csv"
    crimes = pd.read_csv(DATA)
    source = f"synthetic fallback ({type(e).__name__})"

print("source:", source)
print(crimes.shape)
cols = [c for c in ["category", "location.latitude"] if c in crimes.columns]
print(crimes[cols].head())
