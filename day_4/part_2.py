grid = open("input.txt", "r").read().split("\n")[:-1]
# grid = open("sample.txt", "r").read().split("\n")[:-1]

total = 0
row_len = len(grid)
col_len = len(grid[0])

# horizontal
for r, row in enumerate(grid):
  for c, ele in enumerate(row):

    if (c + 2) < col_len and (r + 2) < row_len:
      if grid[r+1][c+1] != "A":
        continue
      # left M
      if grid[r][c] == "M" and grid[r+2][c+2] == "S" and grid[r+2][c] == "M" and grid[r][c+2] == "S":
        total += 1
      # top M
      elif grid[r][c] == "M" and grid[r+2][c+2] == "S" and grid[r+2][c] == "S" and grid[r][c+2] == "M":
        total += 1
      # right M 
      elif grid[r][c] == "S" and grid[r+2][c+2] == "M" and grid[r+2][c] == "S" and grid[r][c+2] == "M":
        total += 1
      # bottom M
      elif grid[r][c] == "S" and grid[r+2][c+2] == "M" and grid[r+2][c] == "M" and grid[r][c+2] == "S":
        total += 1


print(total)

 


