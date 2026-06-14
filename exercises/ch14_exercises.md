# Chapter 14 exercises

## Validation, fairness, and accountability

- Coding task. Take the prediction model you built in Chapter 8 and compute confusion matrices separately for two groups defined by a demographic or area characteristic. Report which fairness criteria hold, which fail, and in which direction.
- Coding task. Construct a synthetic dataset in which two groups have different base rates of the outcome. Show numerically that you can equalise calibration or false positive rates across groups by adjusting thresholds, but not both, and present the trade-off as a plot.
- Write a model card for your Chapter 8 model: intended use, training data and its known biases, performance overall and by group, and the uses for which the model must not be employed. Write it so an affected member of the public could follow it.
- Draft the accountability conditions a police force should be required to meet before deploying a risk model: what must be documented, who reviews it, how an affected person is informed, and how they contest a decision. Compare your conditions against the high-risk requirements of the EU AI Act.

---

Coding tasks above can be started from the matching chapter script (`code/python/ch14_*.py` or `code/r/ch14_*.R`) and the synthetic data in `data/synthetic/`. Where an exercise asks for real data, the data directory README lists open sources you can substitute.
