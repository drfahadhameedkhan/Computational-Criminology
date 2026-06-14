# Chapter 9 exercises

## Spatial analysis and crime mapping

The exercises below assume no prior programming. Read the walkthrough first, then type the code yourself rather than copying it, because typing forces you to notice each step. Both tracks do the same job, so choose the language your department uses. R has the deeper tradition in spatial statistics; Python integrates more easily with general data work. Either is a sound first language for a criminologist.
Work through these in order. The later ones reward the habits the chapter argues for.
- Reproduce Figure 9.1 from any point dataset you can obtain, drawing the points and a density surface side by side. Change the bandwidth twice and write two sentences on how the map changes.
- Compute Moran's I for counts on a 500 m grid and again on a 1000 m grid. Report both, with permutation p-values, and explain any difference using the modifiable areal unit problem.
- Map the local Moran or Getis-Ord results and mark the significant hot spots. Apply a correction for multiple testing and state how many cells survive it.
- Take the busiest ten cells in one month and track them over the next three months. Discuss what regression to the mean implies for an intervention aimed at this month's worst places.
- Write a 300-word methods paragraph reporting your analysis to the standard set out in Chapter 16, naming every choice a reader would need to reproduce it.
These are for discussion and writing, and they do not need a computer.
- A council reports that half of all street robbery falls on two per cent of street segments and proposes saturation patrol there. Set out, as concentration and regression to the mean would, the case for and the case against.
- A predictive system trained on recorded crime sends patrols to the same districts each week. Explain the feedback loop, and propose one change to the data or the design that would weaken it.
- You are asked to map drug offences for a public report. Identify three display choices that would shape how readers judge the affected neighbourhoods, and state the choice you would defend.

---

Coding tasks above can be started from the matching chapter script (`code/python/ch09_*.py` or `code/r/ch09_*.R`) and the synthetic data in `data/synthetic/`. Where an exercise asks for real data, the data directory README lists open sources you can substitute.
