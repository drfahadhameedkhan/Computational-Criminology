# Chapter 16 - Writing and publishing computational criminology
# A bootstrap confidence interval.

set.seed(0)
data <- rnorm(300, mean = 4.0, sd = 1.5)

# --- book code (Chapter 16) ------------------------------------------------
# R: a bootstrap confidence interval
boot <- replicate(2000, mean(sample(data, replace = TRUE)))
quantile(boot, c(0.025, 0.975))
cat("mean =", round(mean(data), 2), "\n")
