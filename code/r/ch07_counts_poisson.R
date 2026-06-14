# Chapter 7 - Statistical foundations
# Crime counts, overdispersion, and a Poisson regression.

# setup: build the same synthetic area frame as the Python version
set.seed(7)
area <- data.frame(deprivation = rnorm(500))
mu <- exp(1.0 + 0.5 * area$deprivation)
area$crimes <- rpois(500, mu)
cat("variance / mean =", round(var(area$crimes) / mean(area$crimes), 2), "\n")

# --- book code (Chapter 7) -------------------------------------------------
# R: the same, moving to negative binomial if dispersion is high
m <- glm(crimes ~ deprivation, data = area, family = poisson)
summary(m)                       # compare residual deviance to its d.f.
# MASS::glm.nb(crimes ~ deprivation, data = area)  # if overdispersed
