# Chapter 15 - Reproducibility and open science
# The three habits: a fixed seed, raw-to-outputs flow, a recorded environment.

# --- book code (Chapter 15) ------------------------------------------------
# R: the same three habits
set.seed(42)                        # repeatable randomness
# read from "data/raw", write to "outputs", never edit the raw files
writeLines(capture.output(sessionInfo()), "session-info.txt")
cat("seed fixed; environment written to session-info.txt\n")
