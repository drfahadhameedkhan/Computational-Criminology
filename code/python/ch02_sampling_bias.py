"""
Chapter 2 - Designing a computational study
Why a biased sampling process pulls an estimate away from the truth, even
with a very large sample. Self-contained.
"""
# --- book code (Chapter 2) -------------------------------------------------
# Python: a population where 12% have offended, then a biased sample
import numpy as np
rng = np.random.default_rng(1)
N = 100_000
offended = rng.random(N) < 0.12          # the hidden truth: 12%
# offenders are less likely to respond to the survey
p_respond = np.where(offended, 0.3, 0.7)
in_sample = rng.random(N) < p_respond
print('true rate   :', round(offended.mean(), 3))
print('sample rate :', round(offended[in_sample].mean(), 3))
