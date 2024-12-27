from collections import deque

# grid = open("sample.txt", "r").read().split("\n")[:-1]
grid = open("input.txt", "r").read().split("\n")[:-1]

start = 0
end = 0
walls = set()
empty = set()
for r, row in enumerate(grid):
  for c, node in enumerate(row):
    if node == "#":
      walls.add(r*1j + c)
    elif node == "S":
      start = r*1j + c
    elif node == "E":
      end = r*1j + c
    elif node == ".":
      empty.add(r*1j + c)

dirs = [1j, -1j, 1, -1]

bfs = deque([(end, 0)])
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
start_scores = {}

# do a normal bfs
while bfs:
  pos, score = bfs.popleft()

  if pos in walls:

    continue

  if pos in start_scores:
    continue
  start_scores[pos] = score

  for dir in dirs:
    bfs.append((pos+dir, score + 1))

normal_score = start_scores[end]

total = 0
empty.add(start)
empty.add(end)
# go through all cheats
# in hindsight prob better to just find all nearest <=20 distance cheats for each point
for spos in empty:
  for epos in empty:

    cheat_time = abs(epos.imag - spos.imag) + abs(epos.real - spos.real)
    # whether allowed cheat using manhatten distance
    if cheat_time > 20:
      continue

    # allowed cheat so check if its good enuf
    new_score = start_scores[spos] + scores[epos] + cheat_time
    saved = normal_score - new_score
    if saved >= 100:
      total += 1

print(total)
