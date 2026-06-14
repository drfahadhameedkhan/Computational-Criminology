# Install the R packages used by the R track of Computational Criminology.
# Run once:  Rscript install.R
# (or open R and source this file)

packages <- c(
  "readr",     # reading data files (Ch 1, 5)
  "tidyr",     # reshaping data (Ch 5)
  "dplyr",     # data manipulation (Ch 6)
  "httr",      # HTTP requests to APIs (Ch 4)
  "jsonlite",  # parsing JSON (Ch 4)
  "tibble",    # tidy data frames (Ch 4)
  "MASS",      # negative binomial regression (Ch 7)
  "sf",        # spatial vector data (Ch 9)
  "spatstat",  # point-pattern analysis (Ch 9)
  "spdep",     # spatial weights and Moran's I (Ch 9)
  "igraph",    # network analysis (Ch 10)
  "quanteda"   # text as data (Ch 12)
)

to_install <- packages[!packages %in% rownames(installed.packages())]
if (length(to_install) > 0) {
  install.packages(to_install, repos = "https://cloud.r-project.org")
} else {
  message("All required R packages are already installed.")
}
