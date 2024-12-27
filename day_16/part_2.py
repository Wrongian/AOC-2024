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

# pos, dir, score, parent, parentdir
bfs = deque([(start, 1, 0, 0, 0)])
scores = {}
rotations = [1j, -1j]
scores[(start, 1)] = 0
best_parent = {}
best_parent[(start, 1)] = [(start, 1)]
best_ends = []
while bfs:
  pos, dir, score, p, pdir = bfs.popleft()

  # check if wall
  if pos in walls:
    continue

  # check if wasted pos
  if (pos, dir) not in scores:
    scores[(pos, dir)] = score
    best_parent[(pos, dir)] = [(p, pdir)]
  else:
    if scores[(pos, dir)] < score:
      continue
    elif scores[(pos, dir)] == score:
      if (p, pdir) not in best_parent[(pos, dir)]:
        best_parent[(pos, dir)].append((p, pdir))
    else:
      scores[(pos, dir)] = score
      best_parent[(pos, dir)] = [(p, pdir)]

  # check for ending position
  if pos == end:
    if score < lowest:
      best_ends = [(end, dir)]
    elif score == lowest:
      if (end, dir) not in best_ends:
        best_ends.append((end, dir))
    lowest = min(lowest, score)
    continue

  # iterate through all moves
  # rotate
  for rotate in rotations:
    ndir = dir*rotate
    npos = pos
    nscore = score + 1000
    bfs.append((npos, ndir, nscore, pos, dir))

  # forward
  ndir = dir
  npos = pos + dir
  nscore = score + 1
  bfs.append((npos, ndir, nscore, pos, dir))

bfs = deque(list(best_ends))
visited = set()
visited.add(start)
while bfs:
  pos, dir = bfs.popleft()
  if pos not in visited:
    visited.add(pos)
  if start == pos:
    continue

  p_arr = best_parent[(pos, dir)]
  # if (pos, dir) == (7j + 5, 1):
  #   print(bfs)
  # print(pos)
  # print(p_arr)
  for p, pdir in p_arr:
    bfs.append((p, pdir))
    # print(bfs)

# print(best_parent[(7j + 5, 1)])
# print(visited)
print(len(visited))

# debug, print maze
"""
with open("out.txt", "w") as f:
  s = ""
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      node = r*1j + c
      if node in walls:
        s += "#"
      elif node in visited:
        s += "0"
      else:
        s += "."
    s += "\n"

  f.write(s)
"""
