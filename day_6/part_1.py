# grid = open("input.txt", "r").read().split("\n")
grid = open("sample.txt", "r").read().split("\n")[:-1]

start = (0, 0)
# get the position of the guard
for r, row in enumerate(grid):
  for c, node in enumerate(row):
    if node == "^":
      start = c + r*1j  # x,y y downwards, x rightwards

max_r = len(grid) - 1
max_c = len(grid[0]) - 1

done = set()

pos = start
# forwards
dir = -1j

done.add(pos)

# while not left the area
while pos.real >= 0 and pos.real >= 0 and pos.real <= max_c and pos.imag <= max_r:
  new_pos = pos + dir

  # check bounds
  if new_pos.real < 0 or new_pos.imag < 0 or new_pos.real > max_c or new_pos.imag > max_r:
    break

  # if obstacle
  if grid[int(new_pos.imag)][int(new_pos.real)] == "#":
    # rotate rightwards
    dir = dir * 1j
    new_pos = pos

  pos = new_pos
  done.add(pos)

print(len(done))
