import networkx as nx
# conns = open("sample.txt", "r").read().split("\n")[:-1]
conns = open("input.txt", "r").read().split("\n")[:-1]

G = nx.Graph()
for conn in conns:
  n1, n2 = conn.split("-")
  G.add_node(n1)
  G.add_node(n2)
  G.add_edge(n1, n2)
  G.add_edge(n2, n1)

best = ()
for clique in nx.find_cliques(G):
  if len(clique) > len(best):
    best = clique

# print(best)
print(",".join(sorted(list(best))))
# print(list(nx.find_cliques(G)))
# print("".join(sorted(list(nx.approximation.max_clique(G)))))
