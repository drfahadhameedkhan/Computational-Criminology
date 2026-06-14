# Chapter 12 - Text as data
# A document-feature matrix. Needs: install.packages("quanteda")

docs <- c("robbery near the station",
          "burglary of a home",
          "robbery and assault near the station")

# --- book code (Chapter 12) ------------------------------------------------
# R: the same with quanteda
library(quanteda)
dfm(tokens(docs))    # a document-feature matrix
