from collections import defaultdict
from collections import deque

# grid = [[c for c in line]
#         for line in open("sample.txt", "r").read().split("\n")[:-1]]

grid = [[c for c in line]
        for line in open("input.txt", "r").read().split("\n")[:-1]]

# prices
prices = defaultdict(int)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

mx = len(grid[0]) - 1
my = len(grid) - 1

# bfs regions
seen = set()
for r, row in enumerate(grid):
  for c, node in enumerate(row):

    if (c, r) in seen:
      continue

    # do a bfs otherwise
    bfs = deque([(c, r, node)])

    # new region
    region = set()
    perimeter = 0
    area = 0
    in_bfs_before = set()

    # bfs
    while len(bfs) > 0:
      x, y, n = bfs.popleft()

      for dx, dy in dirs:
        nx, ny = x+dx, y+dy

        # check bounds
        if nx < 0 or ny < 0 or nx > mx or ny > my:
          continue

        # get new node
        nn = grid[ny][nx]

        # check if node are the same
        if nn != n:
          continue

        # check the region
        if (nx, ny) in region and (x, y) not in region:
          perimeter -= 2

        # check seen
        if (nx, ny) in seen:
          continue

        if (nx, ny, nn) in in_bfs_before:
          continue

        # here means new node same and in bounds and not seen before, means new part of the region
        bfs.append((nx, ny, nn))
        in_bfs_before.add((nx, ny, nn))

      if (x, y) not in region:
        perimeter += 4
        region.add((x, y))
        area += 1

      if (x, y) not in seen:
        seen.add((x, y))

      # print(f"{x}, {y} : {perimeter}")
    prices[node] += perimeter * area


total = sum(prices.values())
print(total)
