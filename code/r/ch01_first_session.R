# Chapter 1 - The shape of computational criminology
# Your first computational session: load a dataset and look at it.
# Run from the repository root after generating the synthetic data.

data_path <- file.path("data", "synthetic", "incidents.csv")

# --- book code (Chapter 1) -------------------------------------------------
# R: install once, then load a crime dataset and look at it
# install.packages("readr")    # run once if readr is not installed
library(readr)
crime <- read_csv(data_path)      # read a file into a table
nrow(crime); ncol(crime)          # how many rows and columns?
summary(crime)                    # a quick description of each column
