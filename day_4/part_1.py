grid = open("input.txt", "r").read().split("\n")[:-1]
# grid = open("sample.txt", "r").read().split("\n")[:-1]

total = 0
row_len = len(grid)
col_len = len(grid[0])

# horizontal
for r, row in enumerate(grid):
  for c, ele in enumerate(row):

    if row[c:c+4] == "XMAS":
      total += 1

    if row[c:c+4][::-1] == "XMAS":
      total += 1
    
    # bottom right diag
    if (c + 3) < col_len and (r + 3) < row_len:
      if grid[r][c] == "X" and grid[r+1][c+1] == "M" and grid[r+2][c+2] == "A"and grid[r+3][c+3] == "S":
        total += 1

    if (c - 3) >= 0 and (r - 3) >= 0:
      if grid[r][c] == "X" and grid[r-1][c-1] == "M" and grid[r-2][c-2] == "A"and grid[r-3][c-3] == "S":
        total += 1   

    # top right diag
    if (c + 3) < col_len and (r - 3) >= 0:
      if grid[r][c] == "X" and grid[r-1][c+1] == "M" and grid[r-2][c+2] == "A"and grid[r-3][c+3] == "S":
        total += 1

    if (c - 3) >= 0 and (r + 3) < row_len:
      if grid[r][c] == "X" and grid[r+1][c-1] == "M" and grid[r+2][c-2] == "A"and grid[r+3][c-3] == "S":
        total += 1


grid_T = zip(*grid)  
# vertical
for r, row in enumerate(grid_T):
  for c, ele in enumerate(row):

    if "".join(row[c:c+4]) == "XMAS":
      total += 1

    if "".join(row[c:c+4][::-1]) == "XMAS":
      total += 1

print(total)

 


