"""
Generate the synthetic datasets used by the worked examples.

The book argues (Chapter 6, Chapter 15) that crime data is sensitive and
should rarely be shared as-is. The companion repository follows that rule:
every example runs on synthetic data that preserves the structure a reader
needs to learn the method, without describing any real person.

Everything here is driven by a fixed seed, so the files regenerate
identically on any machine. Run once from the repository root:

    python data/synthetic/make_synthetic_data.py

Outputs land in data/synthetic/.
"""

from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(SEED)

CATEGORIES = [
    "anti-social-behaviour", "burglary", "robbery", "violent-crime",
    "vehicle-crime", "shoplifting", "criminal-damage-arson", "drugs",
]
DISTRICTS = ["A", "B", "C", "D", "E"]


def make_incidents(n=5000):
    """A month of incident records, with deliberate, realistic missingness."""
    months = pd.date_range("2024-01-01", "2024-01-31", freq="D")
    df = pd.DataFrame({
        # identifiers kept as zero-padded strings on purpose (Chapter 5)
        "crime_id": [f"{i:08d}" for i in range(1, n + 1)],
        "category": rng.choice(CATEGORIES, n,
                               p=[0.30, 0.10, 0.05, 0.18, 0.12, 0.10, 0.08, 0.07]),
        "date": rng.choice(months, n),
        "district": rng.choice(DISTRICTS, n, p=[0.30, 0.25, 0.20, 0.15, 0.10]),
    })
    # coordinates loosely around Liverpool, two soft concentrations
    centre = np.array([53.40, -2.97])
    cluster = rng.random(n) < 0.5
    lat = np.where(cluster,
                   rng.normal(centre[0] + 0.01, 0.012, n),
                   rng.normal(centre[0] - 0.01, 0.018, n))
    lng = np.where(cluster,
                   rng.normal(centre[1] + 0.01, 0.012, n),
                   rng.normal(centre[1] - 0.01, 0.018, n))
    df["location.latitude"] = lat.round(6)
    df["location.longitude"] = lng.round(6)

    # missingness that is NOT random: location missing more often for some
    # districts (a recording artefact, the kind Chapter 5 asks you to profile)
    miss_loc = (df["district"].isin(["D", "E"]) & (rng.random(n) < 0.25)) \
        | (rng.random(n) < 0.04)
    df.loc[miss_loc, ["location.latitude", "location.longitude"]] = np.nan

    # outcome category missing for a fixed share (open data often lacks it)
    df["outcome_category"] = rng.choice(
        ["under investigation", "no suspect identified", "charged", np.nan],
        n, p=[0.25, 0.45, 0.10, 0.20])

    df.to_csv(OUT / "incidents.csv", index=False)
    return df


def make_burglary(n=1200):
    """Burglary points in projected coordinates (British National Grid, EPSG:27700).

    Two genuine concentrations are planted so spatial clustering tests
    (Chapter 9) have something true to find.
    """
    base = np.array([336000, 388000])           # somewhere in NW England, in metres
    n1 = int(n * 0.42)
    n2 = int(n * 0.38)
    n3 = n - n1 - n2
    # clusters wide enough to span several 500 m cells, so neighbouring cells
    # are jointly busy: that is what positive spatial autocorrelation means
    c1 = rng.normal(base + [700, 600], 350, (n1, 2))
    c2 = rng.normal(base + [-800, -500], 400, (n2, 2))
    bg = rng.uniform(base - 1500, base + 1500, (n3, 2))   # diffuse background
    xy = np.vstack([c1, c2, bg])
    rng.shuffle(xy)
    df = pd.DataFrame({"easting": xy[:, 0].round(1),
                       "northing": xy[:, 1].round(1)})
    df.to_csv(OUT / "burglary.csv", index=False)
    return df


def make_ml_table(n=4000):
    """Area-month features and a binary target for the prediction chapters (8, 14).

    A 'group' column lets Chapter 14 compare error rates across groups.
    The target is rare (about 18%), as crime outcomes usually are.
    """
    deprivation = rng.normal(0, 1, n)
    prior_count = rng.poisson(np.exp(0.6 + 0.5 * deprivation))
    density = rng.normal(0, 1, n)
    group = rng.choice(["A", "B"], n, p=[0.6, 0.4])
    # group B is policed more heavily for the same underlying level: this is
    # the proxy problem (Chapter 8) baked in on purpose
    logit = (-2.0 + 0.8 * deprivation + 0.05 * prior_count
             + 0.3 * density + np.where(group == "B", 0.5, 0.0))
    p = 1 / (1 + np.exp(-logit))
    target = (rng.random(n) < p).astype(int)
    df = pd.DataFrame({
        "deprivation": deprivation.round(3),
        "prior_count": prior_count,
        "density": density.round(3),
        "group": group,
        "target": target,
    })
    df.to_csv(OUT / "ml_table.csv", index=False)
    return df


def make_panel():
    """An area-by-period panel for difference-in-differences (Chapter 13).

    A policy switches on in the treated areas at period 6. The true effect
    is a reduction of 8 crimes per area-period.
    """
    areas = range(40)
    periods = range(12)
    rows = []
    for a in areas:
        treated = 1 if a < 20 else 0
        area_fe = rng.normal(60, 8)
        for t in periods:
            post = 1 if t >= 6 else 0
            trend = 1.2 * t                       # common time trend
            effect = -8 if (treated and post) else 0
            crime = (area_fe + trend + effect
                     + rng.normal(0, 4))
            rows.append((a, t, treated, post, round(crime, 1)))
    df = pd.DataFrame(rows, columns=["area", "period", "treated", "post", "crime"])
    df.to_csv(OUT / "panel.csv", index=False)
    return df


if __name__ == "__main__":
    inc = make_incidents()
    bur = make_burglary()
    ml = make_ml_table()
    pan = make_panel()
    print(f"incidents.csv : {inc.shape[0]:>5} rows, {inc.shape[1]} cols")
    print(f"burglary.csv  : {bur.shape[0]:>5} rows, {bur.shape[1]} cols")
    print(f"ml_table.csv  : {ml.shape[0]:>5} rows, {ml.shape[1]} cols "
          f"(target rate {ml.target.mean():.2f})")
    print(f"panel.csv     : {pan.shape[0]:>5} rows, {pan.shape[1]} cols")
    print("All synthetic data written to", OUT)
