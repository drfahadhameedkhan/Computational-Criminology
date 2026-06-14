"""
Chapter 6 - Ethics, privacy, and law
Measure k-anonymity on a small table, then generalise quasi-identifiers to
raise it. Self-contained.
"""
# --- book code (Chapter 6) -------------------------------------------------
# Python: measure k, then generalise to raise it
import pandas as pd
people = pd.DataFrame({
  "dob":["1990-03","1991-07","1990-11","1982-01","1983-09","1981-05"],
  "sex":["M","M","M","F","F","F"],
  "postcode":["AB1 2CD","AB1 3CE","AB1 1CF","CD3 4EF","CD3 5EG","CD3 6EH"]})
qi = ["dob","sex","postcode"]
k = people.groupby(qi).size().min()
print("k before:", k)                      # 1: every record is unique
people["decade"]  = people["dob"].str[:3] + "0s"      # 1990-03 -> 1990s
people["district"]= people["postcode"].str.split().str[0]  # AB1, CD3
k2 = people.groupby(["decade","sex","district"]).size().min()
print("k after :", k2)                     # 3: now each record hides in a crowd
