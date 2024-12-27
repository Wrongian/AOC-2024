from collections import deque

# grid = open("sample.txt", "r").read().split("\n")[:-1]
grid = open("input.txt", "r").read().split("\n")[:-1]

# position of all zeros
zeros = []

# parse grid as ints
new_grid = []
for r, row in enumerate(grid):
  new_row = []
  new_grid.append(new_row)
  for c, node in enumerate(row):
    int_node = int(node)
    new_row.append(int_node)
    if int_node == 0:
      zeros.append((c, r))  # x, y

grid = new_grid

# bounds
mx, my = len(grid[0]) - 1, len(grid) - 1

# ans
trail_sum = 0

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# bfs on each zero/trail
for sx, sy in zeros:
  bfs = deque([(sx, sy)])
  visited_nine = set()
  while len(bfs) > 0:
    x, y = bfs.popleft()
    p = grid[y][x]

    # termination conditions
    if p == 9:
      visited_nine.add((x, y))
      continue

    # propagation
    for dx, dy in dirs:
      nx, ny = x + dx, y + dy

      # check bounds
      if nx > mx or ny > my or nx < 0 or ny < 0:
        continue

      np = grid[ny][nx]

      # check if increasing by 1
      if np == p + 1:
        bfs.append((nx, ny))
  trail_sum += len(visited_nine)

print(trail_sum)
