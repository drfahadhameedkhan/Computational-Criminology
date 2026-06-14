# Chapter 6 - Ethics, privacy, and law
# Measure k-anonymity, then generalise quasi-identifiers to raise it.
# Self-contained.

library(dplyr)
people <- data.frame(
  dob      = c("1990-03","1991-07","1990-11","1982-01","1983-09","1981-05"),
  sex      = c("M","M","M","F","F","F"),
  postcode = c("AB1 2CD","AB1 3CE","AB1 1CF","CD3 4EF","CD3 5EG","CD3 6EH"),
  stringsAsFactors = FALSE)

# --- book code (Chapter 6) -------------------------------------------------
# R: the same check
k <- people %>% count(dob, sex, postcode) %>% summarise(min(n))
people <- people %>%
  mutate(decade = paste0(substr(dob, 1, 3), "0s"),
         district = sub(" .*", "", postcode))
k2 <- people %>% count(decade, sex, district) %>% summarise(min(n))
cat("k before:", k[[1]], "  k after:", k2[[1]], "\n")
