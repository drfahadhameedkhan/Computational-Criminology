"""
Chapter 13 - Causal inference with observational data
Estimate a difference-in-differences effect by ordinary least squares. The
book's snippet assumes a 'panel' frame; here it is loaded from the synthetic
panel, where the true effect is -8.
"""
from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data" / "synthetic" / "panel.csv"
panel = pd.read_csv(DATA)

# --- book code (Chapter 13) ------------------------------------------------
# Python: difference-in-differences by ordinary least squares
import statsmodels.formula.api as smf
# panel: each row is an area-period with treated (0/1) and post (0/1)
model = smf.ols("crime ~ treated * post", data=panel).fit()
print(model.params["treated:post"])   # the difference-in-differences estimate
print("(true effect built into the synthetic data is -8)")
