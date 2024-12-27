from collections import deque

# grid = open("sample.txt", "r").read().split("\n")[:-1]
grid = open("input.txt", "r").read().split("\n")[:-1]

start = 0
end = 0
walls = set()
for r, row in enumerate(grid):
  for c, node in enumerate(row):
    if node == "#":
      walls.add(r*1j + c)
    elif node == "S":
      start = r*1j + c
    elif node == "E":
      end = r*1j + c

max_x = len(grid[0]) - 1
max_y = len(grid) - 1
dirs = [1j, -1j, 1, -1]

# pos, superpower, time_left, score
bfs = deque([(end, 0)])
# all the cheats
cheats = set()
scores = {}

# do a normal bfs
while bfs:
  pos, score = bfs.popleft()

  if pos in walls:

    continue

  if pos in scores:
    continue
  scores[pos] = score

  for dir in dirs:
    bfs.append((pos+dir, score + 1))

bfs = deque([(start, 0)])
# all the cheats
start_scores = {}

# do a normal bfs
while bfs:
  pos, score = bfs.popleft()

  if pos in walls:

    continue

  if pos in start_scores:
    continue
  start_scores[pos] = score

  # identify possible cheats
  # for now only 1 good possible cheat
  for dir1 in dirs:
    for dir2 in dirs:

      npos = pos + dir1 + dir2
      # check bounds
      if npos.real < 0 or npos.imag < 0 or npos.imag > max_y or npos.real > max_x:
        continue
      # check walls
      if npos in walls:
        continue
      # add to possible cheats
      cheats.add((pos, npos))

  for dir in dirs:
    bfs.append((pos+dir, score + 1))

normal_score = start_scores[end]
total = 0
# iterate through all cheats
for spos, epos in cheats:
  new_score = start_scores[epos] + scores[spos]
  saved = normal_score - new_score - 2
  if saved >= 100:
    total += 1

print(total)
