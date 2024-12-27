from collections import defaultdict
# conns = open("sample.txt", "r").read().split("\n")[:-1]
conns = open("input.txt", "r").read().split("\n")[:-1]

conn_dict = defaultdict(set)
for conn in conns:
  n1, n2 = conn.split("-")
  conn_dict[n1].add(n2)
  conn_dict[n2].add(n1)


threes = set()
for n1 in conn_dict.keys():
  for n2 in conn_dict[n1]:
    for n3 in conn_dict[n1]:
      if n2 == n3:
        continue
      if n1[0] != "t" and n2[0] != "t" and n3[0] != "t":
        continue
      if n3 in conn_dict[n2]:
        threes.add(tuple(sorted([n1, n2, n3])))

print(len(threes))
