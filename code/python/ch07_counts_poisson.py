"""
Chapter 7 - Statistical foundations
Crime counts, overdispersion, and a Poisson regression. Self-contained.
"""
# --- book code (Chapter 7) -------------------------------------------------
# Python: check overdispersion, then fit a Poisson model
import numpy as np, pandas as pd
import statsmodels.api as sm, statsmodels.formula.api as smf
rng = np.random.default_rng(7)
area = pd.DataFrame({"deprivation": rng.normal(0, 1, 500)})
mu = np.exp(1.0 + 0.5 * area["deprivation"])     # true relationship
area["crimes"] = rng.poisson(mu)
print("variance / mean =", round(area.crimes.var()/area.crimes.mean(), 2))
m = smf.glm("crimes ~ deprivation", data=area,
            family=sm.families.Poisson()).fit()
print(m.params.round(3))
