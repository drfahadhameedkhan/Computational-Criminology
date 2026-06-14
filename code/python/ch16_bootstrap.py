"""
Chapter 16 - Writing and publishing computational criminology
Report an estimate with a bootstrap confidence interval, the honest way to
show uncertainty. The book's snippet assumes 'data'; here it is a synthetic
sample under a fixed seed.
"""
import numpy as np

# --- setup: a sample to summarise ------------------------------------------
rng_setup = np.random.default_rng(0)
data = rng_setup.normal(4.0, 1.5, 300)

# --- book code (Chapter 16) ------------------------------------------------
# Python: report an estimate with a bootstrap confidence interval
rng = np.random.default_rng(16)
estimates = [np.mean(rng.choice(data, size=len(data), replace=True))
             for _ in range(2000)]          # resample 2000 times
lo, hi = np.percentile(estimates, [2.5, 97.5])
print(f"mean = {data.mean():.2f}, 95% CI [{lo:.2f}, {hi:.2f}]")
