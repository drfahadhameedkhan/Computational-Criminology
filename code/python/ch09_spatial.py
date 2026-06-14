"""
Chapter 9 - Spatial analysis and crime mapping
Read points, estimate a density surface, lay a grid, count, and test for
clustering with Moran's I and a permutation test.

This chapter needs the geospatial stack:
    pip install geopandas libpysal esda matplotlib
On Google Colab these install cleanly. Locally they can be heavy; if they are
missing, the script explains what to install and exits without error.

The book's snippet left the grid construction "to the book site". This is the
book site, so the grid is built in full here.
"""
from pathlib import Path
import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data" / "synthetic" / "burglary.csv"
OUTDIR = Path(__file__).resolve().parents[2] / "figures" / "output"
OUTDIR.mkdir(parents=True, exist_ok=True)

try:
    import geopandas as gpd
    import matplotlib.pyplot as plt
    from libpysal.weights import Queen
    from esda.moran import Moran, Moran_Local
    from shapely.geometry import box
except ImportError as e:
    print("This chapter needs the geospatial stack. Install with:")
    print("    pip install geopandas libpysal esda matplotlib shapely")
    print("Missing:", e.name)
    raise SystemExit(0)

# --- book code: read a CSV of incidents and make spatial points ------------
crime = pd.read_csv(DATA)
pts = gpd.GeoDataFrame(
    crime,
    geometry=gpd.points_from_xy(crime.easting, crime.northing),
    crs=27700)                       # British National Grid: distances in metres

# --- build a 500 m grid and count points per cell --------------------------
xmin, ymin, xmax, ymax = pts.total_bounds
cell = 500.0
cols = np.arange(xmin, xmax + cell, cell)
rows = np.arange(ymin, ymax + cell, cell)
polys = [box(x, y, x + cell, y + cell) for x in cols[:-1] for y in rows[:-1]]
cells = gpd.GeoDataFrame(geometry=polys, crs=27700)
joined = gpd.sjoin(pts, cells, predicate="within", how="left")
counts = joined.groupby("index_right").size()
cells["count"] = cells.index.map(counts).fillna(0).astype(int)
cells = cells[cells["count"].notna()].reset_index(drop=True)

# --- book code: Moran's I with 999 permutations ---------------------------
w = Queen.from_dataframe(cells, use_index=False)   # neighbour relationships
w.transform = 'r'                                  # row-standardise the weights
mi = Moran(cells['count'].values, w, permutations=999)
print('Moran I =', round(mi.I, 3), ' pseudo p =', round(mi.p_sim, 3))

lm = Moran_Local(cells['count'].values, w, permutations=999)
# lm.q gives each cell's quadrant: 1 high-high, 3 low-low, etc.
sig = (lm.p_sim < 0.05) & (lm.q == 1)
print("high-high hot-spot cells (p<0.05):", int(sig.sum()))

# --- save a points + density figure (Figure 9.1 style) --------------------
fig, ax = plt.subplots(1, 2, figsize=(10, 4.5))
pts.plot(ax=ax[0], markersize=3, color="#444")
ax[0].set_title("(a) incidents as points")
ax[0].set_aspect("equal"); ax[0].axis("off")
cells.plot(ax=ax[1], column="count", cmap="viridis", legend=True)
ax[1].set_title("(b) counts per 500 m cell")
ax[1].set_aspect("equal"); ax[1].axis("off")
fig.suptitle("Chapter 9: the same incidents as points and as a grid surface")
fig.tight_layout()
out = OUTDIR / "ch09_points_and_density.png"
fig.savefig(out, dpi=130)
print("figure saved to", out)
