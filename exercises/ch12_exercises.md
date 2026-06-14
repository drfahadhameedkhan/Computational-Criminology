# Chapter 12 exercises

## Text as data

- Coding task. Build a corpus of news coverage of homicides in one city over one year, and compare the distribution of coverage across neighbourhoods with the distribution of recorded homicides. Write 400 words on what the divergence implies for any study using news text as a measure of crime.
- Coding task. Fit a topic model to a corpus of court judgments or police narrative texts, or a synthetic substitute. Hand-label fifty documents yourself, then assess how well the model’s topics correspond to your labels.
- Coding task. Classify the same five hundred documents with a sentiment dictionary and with a supervised classifier trained on two hundred hand-labelled examples. Report where the two methods disagree and inspect twenty disagreements by hand.
- Coding task. Use a large language model to code one hundred text snippets into categories of your design, and have two humans code the same snippets independently. Compute agreement between each pair of coders, human and machine, and write a short protocol stating the conditions under which you would trust the model as a coder.

---

Coding tasks above can be started from the matching chapter script (`code/python/ch12_*.py` or `code/r/ch12_*.R`) and the synthetic data in `data/synthetic/`. Where an exercise asks for real data, the data directory README lists open sources you can substitute.
