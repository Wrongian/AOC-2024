from collections import deque
from heapq import heappush, heappop

# grid = [[c for c in row]
#         for row in open("sample.txt", "r").read().split("\n")[:-1]]
grid = [[c for c in row]
        for row in open("input.txt", "r").read().split("\n")[:-1]]


start = 0
end = 0
walls = set()
for r, row in enumerate(grid):
  for c, node in enumerate(row):
    if node == "S":
      start = r*1j + c
    elif node == "E":
      end = r*1j + c
    elif node == "#":
      walls.add(r*1j + c)

heap = []
rotations = [1j, -1j]
count = 0
heappush(heap, (0, count, start, 1, 0, 0))
visited = set()
parents = {}
end_found = False
while heap:
  score, _, pos, dir, p, pdir = heappop(heap)

  if end_found:
    if pos != end:
      continue
    else:
      parents[(pos, dir)].append((p, pdir))

  if (pos, dir) not in visited:
    parents[(pos, dir)] = [(p, pdir)]
  else:
    parents[(pos, dir)].append((p, pdir))

  if (pos, dir) in visited:
    continue
  visited.add((pos, dir))

  if pos == end:
    end_found = True
    continue

  for rotate in rotations:
    npos = pos
    ndir = dir*rotate
    if npos in walls:
      continue

    if (npos, ndir) in visited:
      continue
    count += 1
    heappush(heap, (score + 1000, count, npos, ndir, pos, dir))

  npos = pos + dir
  ndir = dir
  if npos in walls:
    continue
  if (npos, ndir) in visited:
    continue

  count += 1
  heappush(heap, (score + 1, count, npos, ndir, pos, dir))

bfs = deque([(end, 1), (end, -1), (end, 1j), (end, -1j)])
visited = set()
while bfs:
  pos, dir = bfs.popleft()

  visited.add(pos)

  if (pos, dir) not in parents:
    continue

  p_arr = parents[(pos, dir)]
  for p, pdir in p_arr:
    bfs.append((p, pdir))

print(len(visited) - 1)
