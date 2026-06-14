# Chapter 5 - Cleaning, structuring, and managing data
# Reshape wide to long, read identifiers as text, profile missingness.

data_path <- file.path("data", "synthetic", "incidents.csv")

# --- book code: wide to long with tidyr ------------------------------------
library(tidyr)
wide <- data.frame(area = c("North", "South"), y2019 = c(120, 80), y2020 = c(138, 95))
long <- pivot_longer(wide, cols = c(y2019, y2020),
                     names_to = "year", values_to = "robberies")
print(long)

# --- book code: read identifiers as character, not numeric -----------------
library(readr)
crimes <- read_csv(data_path, col_types = cols(crime_id = col_character()))

# --- book code: share missing per field ------------------------------------
round(colMeans(is.na(crimes)) * 100, 1)
