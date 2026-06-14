# Data

This directory holds the data the worked examples run on, and it follows the
rule the book argues for in Chapter 15: raw data is never edited in place, and
analysis reads from one folder and writes to another.

## `synthetic/`

Every example in the book runs on synthetic data. This is a deliberate choice,
not a convenience. Chapter 6 explains why crime microdata is sensitive and why
sharing it can re-identify the people in it. Synthetic data lets a reader run
the full analysis, see real output, and reproduce every figure, without anyone
having to publish a record about a real victim or suspect.

The files are built by a single script under a fixed seed, so they regenerate
identically on any machine:

```bash
python data/synthetic/make_synthetic_data.py
```

| File | Used by | What it contains |
| --- | --- | --- |
| `incidents.csv` | Chapters 1, 4, 5 | A month of incident records with category, date, district, coordinates, and an outcome field. Missingness is built in on purpose and is not random: location is missing more often in some districts, which is the kind of recording artefact Chapter 5 asks you to profile. |
| `burglary.csv` | Chapter 9 | Burglary points in projected coordinates (British National Grid, EPSG:27700). Two genuine concentrations are planted, so the clustering tests have something true to find. Moran's I on this file is about 0.37 with a permutation p of 0.001. |
| `ml_table.csv` | Chapters 8, 14 | Area-month features (deprivation, prior count, density), a `group` column, and a rare binary `target` (about 19 percent positive). Group B carries extra policing pressure at the same underlying level, so the proxy problem from Chapter 8 and the fairness gap from Chapter 14 are present in the data rather than asserted. |
| `panel.csv` | Chapter 13 | An area-by-period panel where a policy switches on in the treated areas at period six. The true effect is a reduction of eight crimes per area-period, which the difference-in-differences estimator should recover. |

None of these files describes a real person, place, or event. The coordinates
sit loosely near Liverpool only so that distances come out in sensible metres;
they are not real addresses.

## `raw/`

This folder is intentionally empty and is where you place real data you collect
yourself, for example the API responses from the Chapter 4 exercise. Treat
everything here as read-only. Cleaning scripts should read from `raw/` and
write somewhere else, so that the original is always recoverable.

## Open data for the exercises

Several exercises ask you to repeat an analysis on real data. These are open
sources you can substitute. Always check the licence and terms of use before
collecting, as Chapter 4 requires.

- **data.police.uk** (England and Wales). Street-level crime, outcomes, and
  stop-and-search through a free API. This is the source the Chapter 4 example
  calls. https://data.police.uk/docs/
- **Chicago Data Portal**. Incident-level crime since 2001, named in the
  Chapter 5 exercise. https://data.cityofchicago.org/
- **UK Crime Survey for England and Wales** (via the UK Data Service), for the
  victimisation-survey series the Chapter 3 exercise compares against recorded
  crime. https://www.crimesurvey.co.uk/
- **FBI Crime Data Explorer** (United States). National and agency-level
  counts. https://cde.ucr.cjis.gov/
- **INEGI** (Mexico) and other national statistics offices, for readers working
  outside the UK and US.

When you bring in a real source, write a short provenance note next to it
recording the endpoint or URL, the date you collected it, the parameters you
used, and the licence. Chapter 4 explains why that note is part of the data.
