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

        # check seen
        if (nx, ny) in seen:
          continue

        if (nx, ny, nn) in in_bfs_before:
          continue

        # here means new node same and in bounds and not seen before, means new part of the region
        bfs.append((nx, ny, nn))
        in_bfs_before.add((nx, ny, nn))

      if (x, y) not in region:
        region.add((x, y))
        area += 1

      if (x, y) not in seen:
        seen.add((x, y))

      # print(f"{x}, {y} : {perimeter}")
    # from region do raycasting to get the sides
    sides = 0

    # get all unique x,y positions
    x_seen = set()
    y_seen = set()
    for x, y in list(region):
      x_seen.add(x)
      y_seen.add(y)

    # sort
    x_arr = sorted(list(x_seen))
    y_arr = sorted(list(y_seen))

    # so can check raycast out
    x_arr.append(x_arr[-1] + 1)
    y_arr.append(y_arr[-1] + 1)

    # get unique sides
    # raycast x first
    last_hits = set()
    for rx in x_arr:
      is_in = False
      hits = set()  # 0 for in, 1 for out
      # start from lowest y value
      # rx, ry = x_val, y_low

      # raycast
      for ry in y_arr:
        if (rx, ry) in region:
          if is_in == False:
            is_in = True
            hits.add((ry, 0))
        else:
          if is_in == True:
            is_in = False
            hits.add((ry, 1))

      # minus intersection to check if old sides
      sides += len(hits) - len(hits & last_hits)
      last_hits = hits

    # get unique sides
    # raycast x first
    last_hits = set()
    for ry in y_arr:
      is_in = False
      hits = set()  # 0 for in, 1 for out
      # start from lowest y value
      # rx, ry = x_val, y_low

      # raycast
      for rx in x_arr:
        if (rx, ry) in region:
          if is_in == False:
            is_in = True
            hits.add((rx, 0))
        else:
          if is_in == True:
            is_in = False
            hits.add((rx, 1))

      # minus intersection to check if old sides
      sides += len(hits) - len(hits & last_hits)
      last_hits = hits
    prices[node] += sides * area


total = sum(prices.values())
print(total)
