from collections import deque

# grid_raw, dirs = open("sample.txt", "r").read().split("\n\n")
# grid_raw, dirs = open("sample2.txt", "r").read().split("\n\n")
grid_raw, dirs = open("input.txt", "r").read().split("\n\n")

dirs = dirs[:-1].split("\n")
new_dirs = ""
for dir_row in dirs:
  for node in dir_row:
    new_dirs += node
dirs = new_dirs


start = 0
walls = set()
left_boxes = set()
right_boxes = set()
grid = grid_raw.split("\n")

# positive = down right
for r, row in enumerate(grid):
  for c, node in enumerate(row):
    if node == "#":
      walls.add(r*1j + 2*c)
      walls.add(r*1j + 2*c + 1)

    elif node == "O":
      left_boxes.add(r*1j + 2*c)
      right_boxes.add(r*1j + 2*c + 1)

    elif node == "@":
      start = r*1j + 2*c

dir_dict = {
    "<": -1,
    ">": 1,
    "v": 1j,
    "^": -1j,
}

cur = start

for dir in dirs:
  diff = dir_dict[dir]
  next = diff + cur

  # wall in the way
  if next in walls:
    continue

  push_left = deque([])
  push_right = deque([])

  if next in left_boxes or next in right_boxes:
    # there is a box
    # locate all the boxes
    # determinate if it can be pushed
    bfs = deque([cur])
    is_fail = False
    in_bfs = set()

    while bfs:
      node = bfs.popleft()
      next = node + diff

      if next in walls:
        # cannot move if any touch the wall
        is_fail = True
        break

      # has to be one or the other, cannot be both
      # also cannot be visited more than once
      if next in left_boxes:
        if next not in in_bfs:
          bfs.append(next)
          in_bfs.add(next)
          push_left.append(next)

        if next + 1 not in in_bfs:
          bfs.append(next + 1)
          in_bfs.add(next + 1)
          push_right.append(next + 1)

      elif next in right_boxes:
        if next not in in_bfs:
          bfs.append(next)
          in_bfs.add(next)
          push_right.append(next)

        if next - 1 not in in_bfs:
          bfs.append(next - 1)
          in_bfs.add(next - 1)
          push_left.append(next - 1)

    # cannot move boxes so do nothin
    if is_fail:
      continue
    # can move
    else:
      # move all boxes
      # push all boxes if no wall

      # left
      for box in push_left:
        left_boxes.remove(box)

      while push_left:
        box = push_left.pop()
        left_boxes.add(box + diff)

      # right
      for box in push_right:
        right_boxes.remove(box)

      while push_right:
        box = push_right.pop()
        right_boxes.add(box + diff)

      # increment robot if can move boxes
      cur += diff
  else:
    # no box in the way
    cur += diff
    continue

# calculate gps coords
total = int(sum(map(lambda x: x.imag*100 + x.real, left_boxes)))
print(total)
