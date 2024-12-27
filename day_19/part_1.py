from collections import deque
# pats_raw, designs_raw = open("sample.txt", "r").read()[:-1].split("\n\n")
pats_raw, designs_raw = open("input.txt", "r").read()[:-1].split("\n\n")

pats = set(pats_raw.split(", "))
designs = designs_raw.split("\n")


total = 0
for design in designs:
  dp = set()

  # pos correct
  dfs = deque([0])
  s_len = len(design)

  while dfs:
    pos = dfs.pop()

    # termination
    if pos == s_len:
      total += 1
      break

    # pos already done
    if pos in dp:
      continue
    dp.add(pos)

    for i in range(pos + 1, s_len + 1):
      if design[pos:i] in pats:
        if i not in dp:
          dfs.append(i)

print(total)
