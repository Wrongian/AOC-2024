# grid = list(map(list, open("sample.txt", "r").read().split("\n")[:-1]))
grid = list(map(list, open("input.txt", "r").read().split("\n")[:-1]))

start = (0, 0)
# get the position of the guard
for r, row in enumerate(grid):
  for c, node in enumerate(row):
    if node == "^":
      start = c + r*1j  # x,y y downwards, x rightwards

max_r = len(grid) - 1
max_c = len(grid[0]) - 1

pos = start
# forwards
start_dir = -1j


def check_loop(grid, start, start_dir):

  done = set()
  done.add((start, start_dir))

  dir = start_dir
  pos = start

  # while not left the area
  while pos.real >= 0 and pos.real >= 0 and pos.real <= max_c and pos.imag <= max_r:
    new_pos = pos + dir

    # check bounds
    if new_pos.real < 0 or new_pos.imag < 0 or new_pos.real > max_c or new_pos.imag > max_r:
      # not loop
      return False

    # check if loop
    if (new_pos, dir) in done:
      return True

    # if obstacle
    if grid[int(new_pos.imag)][int(new_pos.real)] == "#":
      # rotate rightwards
      dir = dir * 1j
      new_pos = pos

    pos = new_pos

    done.add((pos, dir))

  # not loop
  return False


total = 0
# enumerate over all possible grids
for r, row in enumerate(grid):
  for c, node in enumerate(row):
    if node == ".":
      grid[r][c] = "#"
      # check if you can use the obstacle
      if check_loop(grid, start, start_dir):
        total += 1
      grid[r][c] = "."

print(total)
