# Chapter 13 - Causal inference with observational data
# Difference-in-differences by ordinary least squares.

panel <- read.csv(file.path("data", "synthetic", "panel.csv"))

# --- book code (Chapter 13) ------------------------------------------------
# R: the same model
fit <- lm(crime ~ treated * post, data = panel)
summary(fit)$coefficients["treated:post", ]
# (the true effect built into the synthetic data is -8)
