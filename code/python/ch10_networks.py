"""
Chapter 10 - Network analysis of co-offending
Build a co-offending network and find the broker who controls the path
between two crews. Self-contained.
"""
# --- book code (Chapter 10) ------------------------------------------------
# Python: build the network and find brokers
import networkx as nx
edges = [("A","B"), ("B","C"), ("C","A"), ("C","D"), ("D","E")]  # co-arrests
G = nx.Graph(edges)
bet = nx.betweenness_centrality(G)
print("betweenness:", {k: round(v, 3) for k, v in bet.items()})
print("top broker:", max(bet, key=bet.get))
print("components:", nx.number_connected_components(G))
