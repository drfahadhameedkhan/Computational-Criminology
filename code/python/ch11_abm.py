"""
Chapter 11 - Agent-based modelling and simulation
A minimal routine-activity model: spatial concentration of crime emerges
from movement rules alone, with no hot spot written into the code.
Self-contained (numpy only).
"""
# --- book code (Chapter 11) ------------------------------------------------
# Python: a minimal routine-activity model (numpy only)
import numpy as np
def run(guardian_density, seed=0, size=15, steps=120, n_t=30, n_o=15):
    r = np.random.default_rng(seed)
    n_g = int(guardian_density * size * size)
    T = r.integers(0, size, (n_t, 2))   # targets, fixed
    O = r.integers(0, size, (n_o, 2))   # offenders
    Gd = r.integers(0, size, (n_g, 2))  # guardians
    crimes = 0
    for _ in range(steps):
        O  = (O  + r.integers(-1, 2, O.shape))  % size
        Gd = (Gd + r.integers(-1, 2, Gd.shape)) % size
        guarded = set(map(tuple, Gd))
        for o in O:
            for t in T:
                if o[0]==t[0] and o[1]==t[1] and tuple(o) not in guarded:
                    crimes += 1
    return crimes
if __name__ == "__main__":
    print("few guardians:", run(0.02), " many:", run(0.35))
