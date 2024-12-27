from collections import defaultdict
from collections import deque

# ori_codes = open("sample.txt", "r").read().split("\n")[:-1]
ori_codes = open("input.txt", "r").read().split("\n")[:-1]

# left and up is positive
numeric = {
    "7": 3j + 2,
    "8": 3j + 1,
    "9": 3j,
    "4": 2j + 2,
    "5": 2j + 1,
    "6": 2j,
    "1": 1j + 2,
    "2": 1j + 1,
    "3": 1j,
    "0": 1,
    "A": 0,
}

# left and down is positive
dirs = {
    "A": 0,
    "^": 1,
    ">": 1j,
    "v": 1j + 1,
    "<": 1j + 2
}

dirs2 = {
    "^": -1j,
    ">": -1,
    "v": 1j,
    "<": 1,
}

# for numeric
dirs1 = {
    "^": 1j,
    ">": -1,
    "v": -1j,
    "<": 1,
}


DIR_NUM = 25

# generate all best dir pairs
dir_pairs = defaultdict(list)
for c1 in "<v^>A":
  for c2 in "<v^>A":
    if c1 == c2:
      dir_pairs[(c1, c2)] = [("")]
      continue
    pos = dirs[c1]
    bfs = deque([(pos, "")])
    visited = set()
    max_steps = abs(dirs[c2].imag - dirs[c1].imag) + \
        abs(dirs[c2].real - dirs[c1].real)
    best = []
    while bfs:
      pos, steps = bfs.popleft()

      if pos not in dirs.values():
        continue

      if len(steps) > max_steps:
        continue

      if steps in visited:
        continue

      visited.add(steps)

      if pos == dirs[c2]:
        best.append(steps)

      for c in "<v>^":
        npos = pos + dirs2[c]
        nsteps = steps + c
        bfs.append((npos, nsteps))
    dir_pairs[(c1, c2)] = best

# generate all best numeric pairs
numeric_pairs = defaultdict(list)
for c1 in "7894561230A":
  for c2 in "7894561230A":
    if c1 == c2:
      numeric_pairs[(c1, c2)] = [("")]
      continue
    pos = numeric[c1]
    bfs = deque([(pos, "")])
    visited = set()
    max_steps = abs(numeric[c2].imag - numeric[c1].imag) + \
        abs(numeric[c2].real - numeric[c1].real)
    best = []
    while bfs:
      pos, steps = bfs.popleft()

      if pos not in numeric.values():
        continue

      if len(steps) > max_steps:
        continue

      if steps in visited:
        continue

      visited.add(steps)

      if pos == numeric[c2]:
        best.append(steps)

      for c in "<v>^":
        npos = pos + dirs1[c]
        nsteps = steps + c
        bfs.append((npos, nsteps))
    numeric_pairs[(c1, c2)] = best


memo = {}
# dfs to find min length of all pairs and depth
# num is the number of recursions left


def dfs(c1, c2, depth):

  # termination
  if depth == 0:
    return len(dir_pairs[(c1, c2)][0]) + 1

  if (c1, c2, depth) in memo:
    return memo[(c1, c2, depth)]

  best = float("inf")
  for code in dir_pairs[(c1, c2)]:
    total = 0
    cur = "A"
    for c in code:
      total += dfs(cur, c, depth - 1)
      cur = c
    # include last A
    total += dfs(cur, "A", depth - 1)
    best = min(total, best)
  memo[(c1, c2, depth)] = best
  return best


ans = 0
for code in ori_codes:
  num = int(code[:-1])
  codes = []
  codes.append(code)
  new_codes = []
  # start at A
  cur = "A"
  # numeric first
  for code in codes:
    bfs = deque([""])
    for c in code:
      new_bfs = deque([])
      while bfs:
        s = bfs.popleft()
        for new_s in numeric_pairs[(cur, c)]:
          new_bfs.append(s+new_s + "A")
      bfs = new_bfs
      cur = c
    new_codes += list(bfs)
  codes = new_codes

  best = float("inf")
  for code in codes:
    total = 0
    cur = "A"
    for c in code:
      total += dfs(cur, c, DIR_NUM - 1)
      cur = c
    best = min(total, best)

  # print(code)
  # print(best, num)
  ans += best * num

print(ans)
