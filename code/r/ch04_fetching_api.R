# Chapter 4 - Sources and collection of data
# Fetch a month of street-level crime from the open data.police.uk API.
# Needs network access. Falls back to the synthetic file when offline.

fetch_live <- function() {
  # --- book code (Chapter 4) -----------------------------------------------
  # R: the same request
  library(httr); library(jsonlite); library(tibble)
  res <- GET("https://data.police.uk/api/crimes-street/all-crime",
             query = list(lat = 53.40, lng = -2.97, date = "2024-01"))
  records <- fromJSON(content(res, "text"), flatten = TRUE)
  as_tibble(records)
}

crimes <- tryCatch(fetch_live(), error = function(e) {
  message("API unreachable, using synthetic fallback: ", conditionMessage(e))
  readr::read_csv(file.path("data", "synthetic", "incidents.csv"))
})
cat("rows:", nrow(crimes), "\n")
head(crimes)
