# Chapter 10 - Network analysis of co-offending
# Build a co-offending network and find brokers. Needs: install.packages("igraph")

edges <- data.frame(
  from = c("A","B","C","C","D"),
  to   = c("B","C","A","D","E"),
  stringsAsFactors = FALSE)

# --- book code (Chapter 10) ------------------------------------------------
# R: the same with igraph
library(igraph)
g <- graph_from_data_frame(edges, directed = FALSE)
betweenness(g)
components(g)$no
