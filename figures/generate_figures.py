"""
Regenerate the data-driven figures from the book.

Every figure here is built from code under a fixed seed, so it redraws
identically on any machine. This is the practice the book argues for in
Chapter 15: a figure a reader can reproduce to the last pixel.

Run from the repository root:
    python figures/generate_figures.py

Figures are written to figures/output/ as PNG. Numbering follows the book.
Purely diagrammatic figures (the timeline, the Venn sketch, the crime
funnel, the causal diagram) are described in the book text and are not
reproduced from data here; the figures below are the ones built from
computation.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent / "output"
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"figure.dpi": 130, "font.size": 10,
                     "axes.spreadsheet": False} if False else {"figure.dpi": 130})


def save(fig, name):
    path = OUT / name
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)
    print("saved", path.name)


def fig_2_2_multiple_comparisons():
    """Figure 2.2: chance of at least one false positive rises with the
    number of independent tests at the 5% level."""
    k = np.arange(1, 41)
    p_any = 1 - 0.95 ** k
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(k, p_any, color="#b2182b", lw=2)
    ax.axhline(0.05, ls="--", color="grey")
    ax.axvline(20, ls=":", color="grey")
    ax.annotate(f"20 tests -> {1-0.95**20:.0%}",
                xy=(20, 1 - 0.95 ** 20), xytext=(22, 0.45),
                arrowprops=dict(arrowstyle="->"))
    ax.set_xlabel("number of independent tests")
    ax.set_ylabel("P(at least one false positive)")
    ax.set_title("Figure 2.2  Undisclosed flexibility manufactures findings")
    ax.set_ylim(0, 1)
    save(fig, "fig_2_2_multiple_comparisons.png")


def fig_3_2_diverging_series():
    """Figure 3.2: recorded crime and a survey series diverge, pushed apart
    by a change in recording practice."""
    rng = np.random.default_rng(3)
    years = np.arange(2008, 2024)
    survey = 100 - 1.5 * (years - 2008) + rng.normal(0, 1.5, len(years))
    recorded = 70 - 1.0 * (years - 2008) + rng.normal(0, 1.5, len(years))
    recorded[years >= 2014] += 18          # a recording-practice change
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(years, survey, "-o", label="victimisation survey", color="#2166ac")
    ax.plot(years, recorded, "-s", label="police recorded", color="#b2182b")
    ax.axvline(2014, ls=":", color="grey")
    ax.text(2014.1, ax.get_ylim()[1] * 0.95, "recording change", fontsize=8)
    ax.set_xlabel("year"); ax.set_ylabel("index")
    ax.set_title("Figure 3.2  Two measures of the same offence diverge")
    ax.legend()
    save(fig, "fig_3_2_diverging_series.png")


def fig_7_1_count_distribution():
    """Figure 7.1: crime counts are skewed and over-dispersed, not normal."""
    rng = np.random.default_rng(71)
    pois = rng.poisson(3, 5000)
    nb = rng.negative_binomial(2, 2 / (2 + 5), 5000)
    fig, ax = plt.subplots(1, 2, figsize=(9, 4))
    ax[0].hist(pois, bins=range(0, 15), color="#4393c3", edgecolor="white")
    ax[0].set_title("Poisson (mean = variance)")
    ax[1].hist(nb, bins=range(0, 25), color="#d6604d", edgecolor="white")
    ax[1].set_title("Negative binomial (over-dispersed)")
    for a in ax:
        a.set_xlabel("crimes per area"); a.set_ylabel("areas")
    fig.suptitle("Figure 7.1  Distributions that fit crime counts")
    save(fig, "fig_7_1_count_distribution.png")


def fig_7_2_large_data_trap():
    """Figure 7.2: a trivially small effect crosses the significance line
    once the sample is large enough."""
    rng = np.random.default_rng(72)
    ns = np.unique(np.logspace(1.3, 4.5, 40).astype(int))
    true_effect = 0.03                       # trivially small
    pvals = []
    from scipy import stats
    for n in ns:
        x = rng.normal(0, 1, n)
        y = true_effect * x + rng.normal(0, 1, n)
        r, p = stats.pearsonr(x, y)
        pvals.append(p)
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.semilogx(ns, pvals, "-o", ms=3, color="#762a83")
    ax.axhline(0.05, ls="--", color="grey")
    ax.text(ns[0], 0.07, "p = 0.05", fontsize=8)
    ax.set_xlabel("sample size (log scale)")
    ax.set_ylabel("p-value for a tiny true effect")
    ax.set_title("Figure 7.2  The large-data trap")
    save(fig, "fig_7_2_large_data_trap.png")


def fig_8_1_overfitting():
    """Figure 8.1: as complexity rises, training error keeps falling while
    test error turns upward."""
    c = np.linspace(1, 12, 100)
    train = 1.0 / c + 0.02
    test = 0.08 + 0.0035 * (c - 5) ** 2
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(c, train, label="training error", color="#2166ac", lw=2)
    ax.plot(c, test, label="test error", color="#b2182b", lw=2)
    best = c[np.argmin(test)]
    ax.axvline(best, ls=":", color="grey")
    ax.text(best + 0.2, 0.3, "the gap is the model\nlearning noise", fontsize=8)
    ax.set_xlabel("model complexity"); ax.set_ylabel("error")
    ax.set_title("Figure 8.1  Overfitting")
    ax.legend()
    save(fig, "fig_8_1_overfitting.png")


def fig_8_2_precision_recall():
    """Figure 8.2: precision and recall trade off as the threshold moves,
    for a rare outcome."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import precision_recall_curve
    import pandas as pd
    data = Path(__file__).resolve().parents[1] / "data" / "synthetic" / "ml_table.csv"
    if not data.exists():
        print("skip 8.2: run data/synthetic/make_synthetic_data.py first")
        return
    df = pd.read_csv(data)
    X = df[["deprivation", "prior_count", "density"]]
    y = df["target"]
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.4, random_state=0)
    clf = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
    s = clf.predict_proba(Xte)[:, 1]
    pr, rc, th = precision_recall_curve(yte, s)
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(rc, pr, color="#1b7837", lw=2)
    ax.axhline(yte.mean(), ls="--", color="grey")
    ax.text(0.55, yte.mean() + 0.01, f"base rate = {yte.mean():.2f}", fontsize=8)
    ax.set_xlabel("recall"); ax.set_ylabel("precision")
    ax.set_title("Figure 8.2  Precision and recall trade off for a rare outcome")
    save(fig, "fig_8_2_precision_recall.png")


def fig_9_2_moran_scatter():
    """Figure 9.2: a Moran scatterplot. Each point is a grid cell; the
    positive slope is the clustering."""
    rng = np.random.default_rng(92)
    n = 200
    x = rng.normal(0, 1, n)
    neigh = 0.5 * x + rng.normal(0, 0.7, n)     # neighbours resemble the cell
    fig, ax = plt.subplots(figsize=(5.5, 5))
    ax.scatter(x, neigh, s=12, color="#4393c3", alpha=0.7)
    b = np.polyfit(x, neigh, 1)[0]
    xs = np.linspace(x.min(), x.max(), 2)
    ax.plot(xs, b * xs, color="#b2182b", lw=2, label=f"slope (Moran I) = {b:.2f}")
    ax.axhline(0, color="grey", lw=0.5); ax.axvline(0, color="grey", lw=0.5)
    ax.set_xlabel("standardised count in cell")
    ax.set_ylabel("mean of neighbouring cells")
    ax.set_title("Figure 9.2  Moran scatterplot")
    ax.legend()
    save(fig, "fig_9_2_moran_scatter.png")


def fig_9_4_near_repeat():
    """Figure 9.4: excess risk is highest close in space and soon in time,
    then fades to one."""
    space = np.arange(0, 600, 100)           # metres
    time = np.arange(0, 28, 4)               # days
    S, T = np.meshgrid(space, time)
    risk = 1 + 1.8 * np.exp(-S / 200) * np.exp(-T / 8)
    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    im = ax.imshow(risk, origin="lower", aspect="auto", cmap="magma_r",
                   extent=[space.min(), space.max(), time.min(), time.max()])
    fig.colorbar(im, ax=ax, label="excess risk (1 = chance)")
    ax.set_xlabel("distance from first crime (m)")
    ax.set_ylabel("days after first crime")
    ax.set_title("Figure 9.4  A near-repeat signature")
    save(fig, "fig_9_4_near_repeat.png")


def fig_11_2_sensitivity():
    """Figure 11.2: a sensitivity analysis. Each box is a hundred runs at one
    guardian density. Uses the actual Chapter 11 model."""
    import importlib.util
    ch11 = Path(__file__).resolve().parents[1] / "code" / "python" / "ch11_abm.py"
    spec = importlib.util.spec_from_file_location("ch11", ch11)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    densities = [0.02, 0.10, 0.20, 0.30, 0.40]
    results = [[mod.run(d, seed=s) for s in range(100)] for d in densities]
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.boxplot(results, tick_labels=[f"{d:.2f}" for d in densities])
    ax.set_xlabel("guardian density")
    ax.set_ylabel("offences over 120 steps (100 runs)")
    ax.set_title("Figure 11.2  Crime falls as guardians thicken")
    save(fig, "fig_11_2_sensitivity.png")


def fig_12_1_dtm():
    """Figure 12.1: a document-term matrix as a heatmap."""
    docs = ["robbery near the station",
            "burglary of a home",
            "robbery and assault near the station"]
    vocab = sorted({w for d in docs for w in d.lower().split()})
    dtm = np.array([[d.lower().split().count(w) for w in vocab] for d in docs])
    fig, ax = plt.subplots(figsize=(8, 3))
    im = ax.imshow(dtm, cmap="Blues", aspect="auto")
    ax.set_xticks(range(len(vocab))); ax.set_xticklabels(vocab, rotation=45, ha="right")
    ax.set_yticks(range(len(docs))); ax.set_yticklabels([f"doc {i+1}" for i in range(len(docs))])
    for i in range(dtm.shape[0]):
        for j in range(dtm.shape[1]):
            ax.text(j, i, dtm[i, j], ha="center", va="center", fontsize=8)
    ax.set_title("Figure 12.1  A document-term matrix")
    save(fig, "fig_12_1_dtm.png")


def fig_13_2_did():
    """Figure 13.2: difference-in-differences. The effect is the gap between
    the treated group and its parallel counterfactual."""
    import pandas as pd
    data = Path(__file__).resolve().parents[1] / "data" / "synthetic" / "panel.csv"
    if not data.exists():
        print("skip 13.2: run data/synthetic/make_synthetic_data.py first")
        return
    df = pd.read_csv(data)
    g = df.groupby(["period", "treated"])["crime"].mean().unstack()
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(g.index, g[1], "-o", label="treated", color="#b2182b")
    ax.plot(g.index, g[0], "-s", label="control", color="#2166ac")
    # counterfactual: treated follows control's post-trend
    shift = g[1][5] - g[0][5]
    cf = g[0] + shift
    ax.plot(g.index[6:], cf[6:], "--", color="#b2182b", alpha=0.6,
            label="treated counterfactual")
    ax.axvline(5.5, ls=":", color="grey")
    ax.text(5.6, ax.get_ylim()[0] + 2, "policy on", fontsize=8)
    ax.set_xlabel("period"); ax.set_ylabel("mean crime per area")
    ax.set_title("Figure 13.2  Difference-in-differences")
    ax.legend(fontsize=8)
    save(fig, "fig_13_2_did.png")


def fig_10_1_network():
    """Figure 10.1: a co-offending network with the broker highlighted."""
    import networkx as nx
    edges = [("A", "B"), ("B", "C"), ("C", "A"), ("C", "D"), ("D", "E")]
    G = nx.Graph(edges)
    bet = nx.betweenness_centrality(G)
    broker = max(bet, key=bet.get)
    pos = nx.spring_layout(G, seed=1)
    fig, ax = plt.subplots(figsize=(5.5, 4.5))
    sizes = [3000 * bet[n] + 300 for n in G.nodes]
    colors = ["#b2182b" if n == broker else "#4393c3" for n in G.nodes]
    nx.draw_networkx(G, pos, ax=ax, node_size=sizes, node_color=colors,
                     font_color="white", width=1.5)
    ax.set_title(f"Figure 10.1  Co-offending network (broker = {broker})")
    ax.axis("off")
    save(fig, "fig_10_1_network.png")


if __name__ == "__main__":
    fig_2_2_multiple_comparisons()
    fig_3_2_diverging_series()
    fig_7_1_count_distribution()
    try:
        fig_7_2_large_data_trap()
    except Exception as e:
        print("skip 7.2 (needs scipy):", e)
    fig_8_1_overfitting()
    fig_8_2_precision_recall()
    fig_9_2_moran_scatter()
    fig_9_4_near_repeat()
    fig_10_1_network()
    fig_11_2_sensitivity()
    fig_12_1_dtm()
    fig_13_2_did()
    print("\nAll figures written to", OUT)
