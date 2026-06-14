# Chapter 8 - Machine learning for prediction and classification
# A logistic model judged on a held-out set.

dat <- read.csv(file.path("data", "synthetic", "ml_table.csv"))
dat <- dat[, c("deprivation", "prior_count", "density", "target")]

# --- book code (Chapter 8) -------------------------------------------------
# R: equivalent with a held-out set
set.seed(0)
idx <- sample(nrow(dat), 0.7 * nrow(dat))
fit <- glm(target ~ ., data = dat[idx, ], family = binomial)
p   <- predict(fit, dat[-idx, ], type = "response")

# a simple held-out AUC (no extra packages)
y <- dat$target[-idx]
auc <- function(p, y) {
  r <- rank(p); n1 <- sum(y == 1); n0 <- sum(y == 0)
  (sum(r[y == 1]) - n1 * (n1 + 1) / 2) / (n1 * n0)
}
cat("held-out AUC:", round(auc(p, y), 3), "\n")
