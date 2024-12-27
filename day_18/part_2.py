from collections import deque
# corr_raws = [tuple(map(int, line.split(",")))
#              for line in open("sample.txt", "r").read().split("\n")[:-1]]
corr_raws = [tuple(map(int, line.split(",")))
             for line in open("input.txt", "r").read().split("\n")[:-1]]


corrs = []
for x, y in corr_raws:
  corrs.append(x + y*1j)


max_x = 70
max_y = 70
# max_x = 6
# max_y = 6

start = 0
# end = 70 + 70*1j
end = max_x + max_y*1j
dirs = [1, -1, 1j, -1j]
l = 0
r = len(corrs) - 1
while r > l:
  fallen_corrs = set()
  visited = set()
  bfs = deque([start])
  mid = (l + r)//2
  for i in range(mid + 1):
    fallen_corrs.add(corrs[i])
  while bfs:
    node = bfs.popleft()
    # check bounds
    if node.real > max_x or node.imag > max_y or node.real < 0 or node.imag < 0:
      continue

    if node in fallen_corrs:
      continue

    if node in visited:
      continue
    visited.add(node)

    # print(node)
    # check end
    if node == end:
      break

    for dir in dirs:
      nn = node + dir
      bfs.append(nn)
  if end in visited:
    l = mid + 1
  else:
    r = mid

# print(l, r)
print(corrs[l])

# print(frontiers)
