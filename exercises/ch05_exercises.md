# Chapter 5 exercises

## Cleaning, structuring, and managing data

- Coding task. Load one month of incident records from a city open data portal, such as the Chicago Data Portal. Profile missingness by field and by police district, present the results in a table, and write 300 words on which mechanism of missingness is most plausible for each badly affected field.
- Coding task. In the same dataset, define a rule for identifying duplicate records, apply it, and report how many incidents it removes. Then tighten the rule and loosen it, and report how sensitive the monthly count is to your choice.
- Coding task. Geocode a sample of one hundred address strings from a crime dataset using any geocoding service. Report the match rate, inspect ten failures by hand, and characterise what kinds of address fail.
- Choose a dataset that lacks a data dictionary and write one for its ten most important fields, including the values each field takes and your evidence for what each value means.

---

Coding tasks above can be started from the matching chapter script (`code/python/ch05_*.py` or `code/r/ch05_*.R`) and the synthetic data in `data/synthetic/`. Where an exercise asks for real data, the data directory README lists open sources you can substitute.
