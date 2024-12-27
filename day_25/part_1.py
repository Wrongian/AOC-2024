# lock_keys = open("sample.txt", "r").read()[:-1].split("\n\n")
lock_keys = open("input.txt", "r").read()[:-1].split("\n\n")


locks = []
keys = []
MAX_X = 4
MAX_Y = 6
for lock_key in lock_keys:
  grid = lock_key.split("\n")

  heights = []
  # lock
  if grid[0] == "#" * (MAX_X + 1):
    for x in range(MAX_X + 1):
      height = 0
      for y in range(MAX_Y + 1):
        if grid[y][x] == "#":
          height += 1
        else:
          break
      heights.append(height - 1)
    locks.append(heights)
  # key
  else:
    for x in range(MAX_X + 1):
      height = 0
      for y in range(MAX_Y, -1, -1):
        if grid[y][x] == "#":
          height += 1
        else:
          break
      heights.append(height - 1)
    keys.append(heights)

fits = 0
for lock in locks:
  for key in keys:
    # check if all cols fit
    is_fit = True
    for x in range(MAX_X + 1):
      if (MAX_Y - 1) < (lock[x] + key[x]):
        is_fit = False
        break
    if is_fit:
      fits += 1

print(fits)
