# Chapter 15 exercises

## Reproducibility and open science

- Coding task. Take an analysis you have already completed, in this course or elsewhere, and restructure it as a pipeline: raw data, cleaning script, analysis script, and output, under git, with a single command that regenerates everything. Then have a peer run it on their machine and report every point at which it failed.
- Write a reproducibility README for the project in Exercise 1, recording the environment: language and package versions, the order of execution, expected run time, and the provenance of the raw data.
- Coding task. Create a synthetic version of a sensitive dataset, preserving marginal distributions and the key relationships, and rerun your main analysis on it. Report which findings survive and which do not, and what that implies about sharing the synthetic file.
- Preregister a small, genuinely new analysis, run it, and write up the results with a section reporting every deviation from the preregistration and the reason for it.

---

Coding tasks above can be started from the matching chapter script (`code/python/ch15_*.py` or `code/r/ch15_*.R`) and the synthetic data in `data/synthetic/`. Where an exercise asks for real data, the data directory README lists open sources you can substitute.
