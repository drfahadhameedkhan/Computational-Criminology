# Chapter 3 - Theory, measurement, and the problem of crime data
# Equal true crime, unequal reporting and recording. Self-contained.

# --- book code (Chapter 3) -------------------------------------------------
# R: the same demonstration
true_off <- c(A = 1000, B = 1000)
report   <- c(A = 0.30, B = 0.55)
record   <- c(A = 0.70, B = 0.85)
recorded <- round(true_off * report * record)
recorded                       # A = 210, B = 467
cat("apparent B/A ratio:", round(recorded["B"] / recorded["A"], 2), "\n")
