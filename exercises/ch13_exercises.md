# Chapter 13 exercises

## Causal inference with observational data

- Coding task. Using real or synthetic data on a policy introduced in some areas and not others, estimate a difference-in-differences effect. Plot the pre-intervention trends for both groups, and state in writing whether the plot supports or undermines the parallel trends assumption.
- Coding task. Simulate a sentencing rule that changes at age eighteen and an outcome affected by the sentence. Estimate the effect by regression discontinuity, then introduce sorting at the threshold into your simulation and show what it does to the estimate.
- Draw a causal diagram for the question “does proactive policing reduce neighbourhood crime?” including at least recorded crime, police deployment, and arrests. Identify one variable that looks like a sensible control and is in fact a collider, and explain what conditioning on it would do.
- Coding task. Take an observational estimate from Exercise 1 and conduct a sensitivity analysis: report how strong an unmeasured confounder would need to be, in its associations with treatment and outcome, to reduce the estimate to nothing.

---

Coding tasks above can be started from the matching chapter script (`code/python/ch13_*.py` or `code/r/ch13_*.R`) and the synthetic data in `data/synthetic/`. Where an exercise asks for real data, the data directory README lists open sources you can substitute.
