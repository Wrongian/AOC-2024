from collections import deque

# grid_raw, dirs = open("sample.txt", "r").read().split("\n\n")
grid_raw, dirs = open("input.txt", "r").read().split("\n\n")

dirs = dirs[:-1].split("\n")
new_dirs = ""
for dir_row in dirs:
  for node in dir_row:
    new_dirs += node
dirs = new_dirs


start = 0
walls = set()
boxes = set()
grid = grid_raw.split("\n")

# positive = down right
for r, row in enumerate(grid):
  for c, node in enumerate(row):
    if node == "#":
      walls.add(r*1j + c)

    elif node == "O":
      boxes.add(r*1j + c)

    elif node == "@":
      start = r*1j + c

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

  to_push = deque([])

  if next in boxes:
    # there is a box
    # locate all the boxes

    while next in boxes:
      to_push.append(next)
      next += diff

    if next not in walls:
      # push all boxes in no wall
      for box in to_push:
        boxes.remove(box)

      while to_push:
        box = to_push.pop()
        boxes.add(box + diff)

      # increment robot if can move boxes
      cur = cur+diff
    else:
      # wall
      continue

  else:
    # no box in the way
    cur = next
    continue

# calculate gps coords
total = int(sum(map(lambda x: x.imag*100 + x.real, boxes)))
print(total)
