# grid = open("sample.txt", "r").read().split("\n")[:-1]
grid = open("input.txt", "r").read().split("\n")[:-1]

max_y = len(grid) - 1
max_x = len(grid[0]) - 1

# get unique frequencies
unique_freqs = {}
for r, row in enumerate(grid):
  for c, node in enumerate(row):
    if not node == ".":
      if node not in unique_freqs:
        unique_freqs[node] = []
      unique_freqs[node].append((c, r))  # x, y


antinodes = set()


def antinode_positions(p1, p2):
  dx = p1[0] - p2[0]
  dy = p1[1] - p2[1]
  inc = 0
  while True:
    nx, ny = p2[0] - dx*inc, p2[1] - dy*inc

    # check if bounds
    if nx < 0 or ny < 0 or nx > max_y or ny > max_y:
      break

    antinodes.add((nx, ny))

    inc += 1


# get all antinodes for each freq
for freq_arr in unique_freqs.values():
  # permute
  for freq1 in freq_arr:
    for freq2 in freq_arr:

      # if same
      if freq1 == freq2:
        continue

      antinode_positions(freq1, freq2)

print(len(antinodes))
