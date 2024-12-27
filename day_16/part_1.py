from collections import deque
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

lowest = float("inf")

# pos, dir, score
bfs = deque([(start, 1, 0)])
scores = {}
rotations = [1j, -1j]
scores[(start, 1)] = 0
while bfs:
  pos, dir, score = bfs.popleft()

  # check if wall
  if pos in walls:
    continue

  # check if wasted pos
  if (pos, dir) not in scores:
    scores[(pos, dir)] = score
  else:
    if scores[(pos, dir)] < score:
      continue
    scores[(pos, dir)] = score

  # check for ending position
  if pos == end:
    lowest = min(lowest, score)

  # iterate through all moves
  # rotate
  for rotate in rotations:
    ndir = dir*rotate
    npos = pos
    nscore = score + 1000
    bfs.append((npos, ndir, nscore))

  # forward
  ndir = dir
  npos = pos + dir
  nscore = score + 1
  bfs.append((npos, ndir, nscore))


print(lowest)
