from itertools import combinations
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

# max possible degree of node to brute force
max_degree = 0
for n in conn_dict.keys():
  max_degree = max(max_degree, len(conn_dict[n]))

for i in range(max_degree, 1, -1):
  print(i)
  combs = combinations(nodes, i)
  found = False
  for comb in combs:
    is_conn = True
    pairs = combinations(comb, 2)
    for n1, n2 in pairs:
      if n1 not in conn_dict[n2]:
        is_conn = False
        break
    if is_conn:
      print("".join(sorted(list(comb))))
      found = True
      break
  if found == True:
    break
