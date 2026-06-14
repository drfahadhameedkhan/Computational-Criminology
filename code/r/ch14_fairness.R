# Chapter 14 - Validation, fairness, and accountability
# Error rates by group, from a held-out classifier.

dat <- read.csv(file.path("data", "synthetic", "ml_table.csv"))
set.seed(0)
idx <- sample(nrow(dat), 0.6 * nrow(dat))
fit <- glm(target ~ deprivation + prior_count + density,
           data = dat[idx, ], family = binomial)
test <- dat[-idx, ]
test$score <- predict(fit, test, type = "response")

# --- book code (Chapter 14) ------------------------------------------------
# R: the same confusion-matrix logic, per group
rates <- function(y, score, t = 0.5) {
  pred <- score >= t
  tp <- sum(pred & y == 1); fp <- sum(pred & y == 0)
  fn <- sum(!pred & y == 1); tn <- sum(!pred & y == 0)
  c(FPR = fp / (fp + tn), FNR = fn / (fn + tp), precision = tp / (tp + fp))
}
A <- subset(test, group == "A"); B <- subset(test, group == "B")
print(round(rates(A$target, A$score), 2))
print(round(rates(B$target, B$score), 2))
