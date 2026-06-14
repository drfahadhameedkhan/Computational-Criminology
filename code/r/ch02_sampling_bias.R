# Chapter 2 - Designing a computational study
# A biased sampling process pulls an estimate away from the truth.
# Self-contained.

# --- book code (Chapter 2) -------------------------------------------------
# R: the same simulation
set.seed(1)
N <- 100000
offended <- runif(N) < 0.12
p_respond <- ifelse(offended, 0.3, 0.7)
in_sample <- runif(N) < p_respond
round(mean(offended), 3)              # true rate
round(mean(offended[in_sample]), 3)   # biased sample rate
