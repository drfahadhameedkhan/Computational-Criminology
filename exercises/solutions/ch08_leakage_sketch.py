"""
Chapter 8, Exercise 2 (sketch): introduce leakage on purpose and watch the
held-out AUC inflate. Run from the repository root after building the data.

This is a scaffold, not a model answer. It shows the mechanism; the 200 words
the exercise asks for, on how this leak would look in a real project where
no one introduced it deliberately, are yours to write.
"""
from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

df = pd.read_csv(Path("data/synthetic/ml_table.csv"))
y = df["target"]
honest = df[["deprivation", "prior_count", "density"]].copy()

# A leaked feature: something recorded AFTER the outcome is known, then fed in
# as if it were available at prediction time. Here a "flagged for review" marker
# that mostly fires when the target is positive. This is the most common real
# leak: a field that only exists because the outcome already happened, such as
# "case referred" when predicting reoffending, or a post-hoc risk note.
import numpy as np
rng = np.random.default_rng(0)
leaked = honest.copy()
leaked["flagged_for_review"] = np.where(
    rng.random(len(y)) < 0.85, y, 1 - y)   # agrees with the outcome 85% of the time

def auc_for(X):
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
    clf = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
    return roc_auc_score(yte, clf.predict_proba(Xte)[:, 1])

print(f"honest AUC : {auc_for(honest):.3f}")
print(f"leaked AUC : {auc_for(leaked):.3f}")
print("the gain is information from the test rows that a real model "
      "would not have at prediction time")
