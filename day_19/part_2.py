# pats_raw, designs_raw = open("sample.txt", "r").read()[:-1].split("\n\n")
pats_raw, designs_raw = open("input.txt", "r").read()[:-1].split("\n\n")

pats = set(pats_raw.split(", "))
designs = designs_raw.split("\n")


total = 0
for design in designs:

  dp = [0 for i in range(len(design) + 1)]

  for i in range(len(design)):
    for j in range(i + 1, len(design) + 1):
      if design[i: j] in pats:
        if i == 0 and dp[i] == 0:
          dp[j] += 1
        else:
          dp[j] += dp[i]

  total += dp[len(design)]


print(total)
