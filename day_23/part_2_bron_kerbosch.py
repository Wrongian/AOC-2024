from collections import defaultdict
# conns = open("sample.txt", "r").read().split("\n")[:-1]
conns = open("input.txt", "r").read().split("\n")[:-1]

conn_dict = defaultdict(set)
nodes = set()
for conn in conns:
  n1, n2 = conn.split("-")
  conn_dict[n1].add(n2)
  conn_dict[n2].add(n1)
  nodes.add(n1)
  nodes.add(n2)

max_clique = set()


def bron_kerbosch(cur, candidates, done):
  global max_clique
  # clique found
  if len(candidates) == 0:
    if len(cur) > len(max_clique):
      max_clique = cur
      return

  for node in list(candidates):
    bron_kerbosch(cur | {node}, candidates &
                  conn_dict[node], done & conn_dict[node])
    done.add(node)
    candidates.remove(node)


bron_kerbosch(set(), nodes, set())

print(",".join(sorted(list(max_clique))))
