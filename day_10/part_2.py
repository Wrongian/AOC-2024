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
ratings = 0

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# bfs on each zero/trail
for sx, sy in zeros:
  bfs = deque([(sx, sy)])
  trails = 0
  while len(bfs) > 0:
    x, y = bfs.popleft()
    p = grid[y][x]

    # termination conditions
    if p == 9:
      trails += 1
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
  ratings += trails

print(ratings)
