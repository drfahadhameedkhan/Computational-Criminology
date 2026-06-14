# Chapter 8 exercises

## Machine learning for prediction and classification

- Coding task. Using two years of incident data aggregated to small areas and months, build a model predicting whether each area exceeds its median burglary count next month. Use a strictly temporal split. Compare your model against the baseline “same as last month”, and report whether the machinery earns its complexity.
- Coding task. Deliberately introduce leakage into the same task, for example by including a feature computed over the full period. Report what happens to the test metrics, then write 200 words on how this leak would look in a real project where no one had introduced it on purpose.
- Coding task. Evaluate your Exercise 1 model using accuracy, AUC, and precision-recall at the decision threshold a police force could actually act on. Explain which measure you would report to a commander and why.
- Your labels are arrests. Design a label audit: name two independent sources of evidence you could use to estimate how far arrest diverges from offending for your offence type, and what pattern in that divergence would make the model unacceptable to deploy.

---

Coding tasks above can be started from the matching chapter script (`code/python/ch08_*.py` or `code/r/ch08_*.R`) and the synthetic data in `data/synthetic/`. Where an exercise asks for real data, the data directory README lists open sources you can substitute.
