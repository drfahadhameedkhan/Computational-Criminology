# Computational Criminology: Companion Repository

Code, data, and figures for **Computational Criminology: Research Methods,
Ethics, and Reproducible Practice with R and Python** by Dr Fahad Hameed Khan.

[![tests](https://github.com/drfahadhameedkhan/computational-criminology/actions/workflows/tests.yml/badge.svg)](https://github.com/drfahadhameedkhan/computational-criminology/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/code%20license-MIT-blue.svg)](LICENSE)

This repository lets a reader run every worked example in the book, reproduce
every data-driven figure, and start each coding exercise from a working base.
It is built to the standard the book itself argues for in Chapter 15: a fixed
seed, a clean separation of raw data from outputs, a recorded software
environment, and an analysis a stranger can rebuild from the materials alone.

Every example runs on synthetic data. This is deliberate. Chapter 6 explains
why crime microdata is sensitive and why publishing it can re-identify the
people in it, so the repository shares what can safely be shared, which is the
code and a synthetic stand-in that preserves the structure each method needs.
Nothing here describes a real person, place, or event.

The book teaches each method in both Python and R. Both tracks are here, and
they do the same job, so you can follow in whichever language your department
favours.

## Quick start

The fastest way in is Google Colab, which needs no local install. Open any
chapter notebook with the badge in the table below, run the first cell, and the
notebook will fetch this repository, install what the chapter needs, build the
synthetic data, and run the code.

To work locally with Python:

```bash
git clone https://github.com/drfahadhameedkhan/computational-criminology.git
cd computational-criminology
pip install -r requirements.txt
python data/synthetic/make_synthetic_data.py   # build the datasets once
python code/python/ch08_prediction.py           # run any chapter
```

To work locally with R:

```bash
Rscript install.R                                # install the R packages once
Rscript code/r/ch08_prediction.R
```

The spatial chapter (Chapter 9) needs an extra geospatial stack. Install it
with `pip install -r requirements-spatial.txt`, or use the conda environment in
`environment.yml`, which includes everything.

## What is in here

The repository is organised so that each part of the book maps to a folder.

```
computational-criminology/
├── notebooks/        one Colab notebook per chapter (Python)
├── code/python/      one runnable script per chapter (Python)
├── code/r/           the matching script per chapter (R)
├── data/synthetic/   the datasets, plus the script that builds them
├── data/raw/         where you put real data you collect (kept empty)
├── figures/          the script that regenerates every data-driven figure
├── exercises/        the exercise prompts from each chapter
└── exercises/solutions/  starting scaffolds for the coding tasks
```

## Chapter map

Each row links a chapter to its notebook, its Python and R scripts, and its
exercises. The Colab links work once you have pushed the repository to your own
account and replaced `drfahadhameedkhan`.

| Ch | Title | Colab | Python | R | Exercises |
| --- | --- | --- | --- | --- | --- |
| 1 | The shape of computational criminology | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch01_first_session.ipynb) | [py](code/python/ch01_first_session.py) | [R](code/r/ch01_first_session.R) | [md](exercises/ch01_exercises.md) |
| 2 | Designing a computational study | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch02_sampling_bias.ipynb) | [py](code/python/ch02_sampling_bias.py) | [R](code/r/ch02_sampling_bias.R) | [md](exercises/ch02_exercises.md) |
| 3 | Theory, measurement, and the problem of crime data | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch03_recording_pipeline.ipynb) | [py](code/python/ch03_recording_pipeline.py) | [R](code/r/ch03_recording_pipeline.R) | [md](exercises/ch03_exercises.md) |
| 4 | Sources and collection of data | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch04_fetching_api.ipynb) | [py](code/python/ch04_fetching_api.py) | [R](code/r/ch04_fetching_api.R) | [md](exercises/ch04_exercises.md) |
| 5 | Cleaning, structuring, and managing data | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch05_cleaning.ipynb) | [py](code/python/ch05_cleaning.py) | [R](code/r/ch05_cleaning.R) | [md](exercises/ch05_exercises.md) |
| 6 | Ethics, privacy, and law | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch06_k_anonymity.ipynb) | [py](code/python/ch06_k_anonymity.py) | [R](code/r/ch06_k_anonymity.R) | [md](exercises/ch06_exercises.md) |
| 7 | Statistical foundations | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch07_counts_poisson.ipynb) | [py](code/python/ch07_counts_poisson.py) | [R](code/r/ch07_counts_poisson.R) | [md](exercises/ch07_exercises.md) |
| 8 | Machine learning for prediction and classification | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch08_prediction.ipynb) | [py](code/python/ch08_prediction.py) | [R](code/r/ch08_prediction.R) | [md](exercises/ch08_exercises.md) |
| 9 | Spatial analysis and crime mapping | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch09_spatial.ipynb) | [py](code/python/ch09_spatial.py) | [R](code/r/ch09_spatial.R) | [md](exercises/ch09_exercises.md) |
| 10 | Network analysis of co-offending | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch10_networks.ipynb) | [py](code/python/ch10_networks.py) | [R](code/r/ch10_networks.R) | [md](exercises/ch10_exercises.md) |
| 11 | Agent-based modelling and simulation | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch11_abm.ipynb) | [py](code/python/ch11_abm.py) | [note](code/r/ch11_abm_README.md) | [md](exercises/ch11_exercises.md) |
| 12 | Text as data | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch12_text.ipynb) | [py](code/python/ch12_text.py) | [R](code/r/ch12_text.R) | [md](exercises/ch12_exercises.md) |
| 13 | Causal inference with observational data | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch13_did.ipynb) | [py](code/python/ch13_did.py) | [R](code/r/ch13_did.R) | [md](exercises/ch13_exercises.md) |
| 14 | Validation, fairness, and accountability | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch14_fairness.ipynb) | [py](code/python/ch14_fairness.py) | [R](code/r/ch14_fairness.R) | [md](exercises/ch14_exercises.md) |
| 15 | Reproducibility and open science | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch15_reproducibility.ipynb) | [py](code/python/ch15_reproducibility.py) | [R](code/r/ch15_reproducibility.R) | [md](exercises/ch15_exercises.md) |
| 16 | Writing and publishing computational criminology | [open](https://colab.research.google.com/github/drfahadhameedkhan/computational-criminology/blob/main/notebooks/ch16_bootstrap.ipynb) | [py](code/python/ch16_bootstrap.py) | [R](code/r/ch16_bootstrap.R) | [md](exercises/ch16_exercises.md) |

Chapter 11 has no paired R snippet in the book, because the agent-based model
is presented in Python. The note in the R folder explains the options for an R
reader.

## Figures

The data-driven figures regenerate from a single script:

```bash
python figures/generate_figures.py
```

Each one is built from code under a fixed seed, so it redraws identically on
any machine. The output lands in `figures/output/` and is committed to the
repository so you can browse the figures without running anything. The purely
diagrammatic figures from the book, such as the crime funnel and the causal
diagrams, are described in the text and are not reproduced from data here.

## How the examples stay correct

Several snippets in the book assume a dataset or a variable is already in hand,
because the text is teaching a method rather than a pipeline. In this
repository each script first loads the relevant synthetic file, then runs the
book's code unchanged. The setup lines are marked, so it is always clear which
lines are from the book and which prepare the data.

The synthetic data is calibrated so the methods recover what they should. The
difference-in-differences estimate comes out near its true value of minus
eight, the Poisson regression recovers its true slope of one half, and Moran's
I on the burglary points is about 0.37 with a permutation p of 0.001. These are
not coincidences; the generator plants those truths so the worked examples have
something real to find.

## Testing

A GitHub Actions workflow runs on every push. It rebuilds the synthetic data,
runs every lightweight chapter script, and regenerates the figures, so a broken
example is caught before anyone else runs it. The spatial chapter runs in a
separate job that is allowed to fail without blocking the rest, because its
geospatial dependencies are heavy to install. You can run the same checks
locally:

```bash
python data/synthetic/make_synthetic_data.py
for f in code/python/ch0[1-8]_*.py code/python/ch1[0-6]_*.py; do python "$f"; done
python figures/generate_figures.py
```

## Licence and citation

The code is released under the MIT Licence (see `LICENSE`). The prose, figures,
and teaching text drawn from the book remain under copyright and are shared for
teaching and study under CC BY-NC 4.0 (see `LICENSE-content`).

If you use this material, please cite the book and this repository. A
machine-readable citation is in `CITATION.cff`.

## A note before you replace drfahadhameedkhan

Several links and one configuration line contain the placeholder
`drfahadhameedkhan`. Once you have created the repository under your own account,
replace that placeholder everywhere so the Colab badges and the clone commands
point at your copy. The setup guide in `SETUP_GITHUB.md` walks through this and
the rest of the steps to get the repository live and tested on your profile.
