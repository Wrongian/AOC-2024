from collections import deque
# corr_raws = [tuple(map(int, line.split(",")))
#              for line in open("sample.txt", "r").read().split("\n")[:-1]]
corr_raws = [tuple(map(int, line.split(",")))
             for line in open("input.txt", "r").read().split("\n")[:-1]]


corr = set()
# total_bytes = 12
total_bytes = 1024
bytes = 0
for x, y in corr_raws:
  corr.add(x + y*1j)
  bytes += 1
  if bytes == total_bytes:
    break

# print(corr)

max_x = 70
max_y = 70
# max_x = 6
# max_y = 6

start = 0
# end = 70 + 70*1j
end = max_x + max_y*1j
bfs = deque([start])
visited = set()
frontiers = 0
dirs = [1, -1, 1j, -1j]
while True:
  new_bfs = deque([])
  while bfs:
    node = bfs.popleft()
    # check bounds
    if node.real > max_x or node.imag > max_y or node.real < 0 or node.imag < 0:
      continue

    if node in corr:
      continue

    if node in visited:
      continue
    visited.add(node)

    # print(node)
    # check end
    if node == end:
      print(frontiers)
      break

    for dir in dirs:
      nn = node + dir
      new_bfs.append(nn)

  bfs = new_bfs
  # print(bfs)
  if len(bfs) == 0:
    break
  frontiers += 1

# print(frontiers)
