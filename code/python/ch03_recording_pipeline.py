"""
Chapter 3 - Theory, measurement, and the problem of crime data
Equal true crime, unequal reporting and recording, produces an apparent
gap between two areas. Self-contained.
"""
# --- book code (Chapter 3) -------------------------------------------------
# Python: equal true crime, unequal reporting and recording
true_offences = {'A': 1000, 'B': 1000}   # the same in both areas
report_prob   = {'A': 0.30, 'B': 0.55}   # area B reports more
record_prob   = {'A': 0.70, 'B': 0.85}   # and is recorded more
recorded = {a: round(true_offences[a]*report_prob[a]*record_prob[a])
            for a in true_offences}
print(recorded)                          # {'A': 210, 'B': 467}
print('apparent B/A ratio:', round(recorded['B']/recorded['A'], 2))
