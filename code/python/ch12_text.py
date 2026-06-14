"""
Chapter 12 - Text as data
Turn a tiny corpus into a document-term matrix by hand, so the structure
behind every text method is visible. Self-contained.
"""
# --- book code (Chapter 12) ------------------------------------------------
# Python: a document-term matrix without heavy libraries
docs = ["robbery near the station",
        "burglary of a home",
        "robbery and assault near the station"]
vocab = sorted({w for d in docs for w in d.lower().split()})
dtm = [[d.lower().split().count(w) for w in vocab] for d in docs]
print(vocab)
for row in dtm: print(row)
