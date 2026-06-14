"""
Chapter 8 - Machine learning for prediction and classification
A classifier judged honestly on held-out data, with measures that survive a
rare outcome. The book's snippet assumes 'features' and 'target' already
exist; here they are loaded from the synthetic ml_table.
"""
from pathlib import Path
import pandas as pd

# --- setup: features and target from the synthetic table -------------------
DATA = Path(__file__).resolve().parents[2] / "data" / "synthetic" / "ml_table.csv"
df = pd.read_csv(DATA)
features = df[["deprivation", "prior_count", "density"]]
target = df["target"]

# --- book code (Chapter 8) -------------------------------------------------
# Python: a classifier judged on held-out data
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, precision_score, recall_score
X_tr, X_te, y_tr, y_te = train_test_split(features, target,
                          test_size=0.3, random_state=0)   # hold out a test set
clf = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
p = clf.predict_proba(X_te)[:, 1]                # predicted probabilities
print("AUC      :", round(roc_auc_score(y_te, p), 3))
pred = (p >= 0.5)
print("precision:", round(precision_score(y_te, pred, zero_division=0), 3))
print("recall   :", round(recall_score(y_te, pred, zero_division=0), 3))

# --- exercise hint: leakage on purpose -------------------------------------
# Adding a feature computed over the whole period (including the test rows)
# inflates the AUC. Uncomment to see the effect:
# leaked = (target.groupby(df["group"]).transform("mean"))
# ... refit with 'leaked' included and compare the AUC.
