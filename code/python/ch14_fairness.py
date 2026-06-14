"""
Chapter 14 - Validation, fairness, and accountability
Error rates by group. The book's snippet assumes group arrays already exist;
here a Chapter 8 classifier is trained, then scored separately for two
groups carried in the synthetic table.
"""
from pathlib import Path
import numpy as np, pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# --- setup: train the Chapter 8 model, split the test set by group ---------
DATA = Path(__file__).resolve().parents[2] / "data" / "synthetic" / "ml_table.csv"
df = pd.read_csv(DATA)
X = df[["deprivation", "prior_count", "density"]]
y = df["target"].values
g = df["group"].values
Xtr, Xte, ytr, yte, gtr, gte = train_test_split(X, y, g, test_size=0.4,
                                                random_state=0)
clf = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
s = clf.predict_proba(Xte)[:, 1]
yA, sA = yte[gte == "A"], s[gte == "A"]
yB, sB = yte[gte == "B"], s[gte == "B"]

# --- book code (Chapter 14) ------------------------------------------------
# Python: fairness metrics by group
def group_rates(y, score, threshold=0.5):
    pred = score >= threshold
    tp = np.sum(pred & (y==1)); fp = np.sum(pred & (y==0))
    fn = np.sum(~pred & (y==1)); tn = np.sum(~pred & (y==0))
    return dict(FPR=fp/(fp+tn), FNR=fn/(fn+tp),
                precision=tp/(tp+fp) if tp+fp else 0)
print("Group A:", {k: round(v,2) for k,v in group_rates(yA, sA).items()})
print("Group B:", {k: round(v,2) for k,v in group_rates(yB, sB).items()})
