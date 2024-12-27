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


def heuristic(p):
  global end
  return abs(end.imag - p.imag) + abs(end.real-p.real)


heap = []
rotations = [1j, -1j]
count = 0
heappush(heap, (heuristic(start), 0, count, start, 1))
"""heuristic is manhantten distance to end"""
visited = set()
while True:
  f, score, _, pos, dir = heappop(heap)

  if (pos, dir) in visited:
    continue
  visited.add((pos, dir))

  if pos == end:
    print(score)
    break

  for rotate in rotations:
    npos = pos
    ndir = dir*rotate
    if npos in walls:
      continue

    if (npos, ndir) in visited:
      continue
    count += 1
    heappush(heap, (score + 1000 + heuristic(npos),
             score + 1000, count, npos, ndir))

  npos = pos + dir
  ndir = dir
  if npos in walls:
    continue
  if (npos, ndir) in visited:
    continue

  count += 1
  heappush(heap, (score + 1000 + heuristic(npos), score + 1, count, npos, ndir))
