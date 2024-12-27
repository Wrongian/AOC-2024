# regs, instrs_raw = open("sample.txt", "r").read()[:-1].split("\n\n")
regs, instrs_raw = open("input.txt", "r").read()[:-1].split("\n\n")

out = []

regs_raw = regs.split(": ")
a = int(regs_raw[1].split("\n")[0])
b = int(regs_raw[2].split("\n")[0])
c = int(regs_raw[3].split("\n")[0])

instrs = list(map(int, instrs_raw.split(": ")[1].split(",")))
p = 0
instrs_len = len(instrs)
while p < instrs_len:
  op = instrs[p]

  # combo
  if op not in [1]:
    raw_comb = instrs[p+1]
    if raw_comb in [0, 1, 2, 3]:
      comb = raw_comb
    elif raw_comb == 4:
      comb = a
    elif raw_comb == 5:
      comb = b
    elif raw_comb == 6:
      comb = c
    elif raw_comb == 7:
      pass

  if op == 0:
    a = int(a/(2**comb))
    p += 2
  elif op == 1:
    b = b ^ instrs[p+1]
    p += 2
  elif op == 2:
    b = comb % 8
    p += 2
  elif op == 3:
    if a != 0:
      p = instrs[p + 1]
    else:
      p += 2
  elif op == 4:
    b = b ^ c
    p += 2
  elif op == 5:
    out.append(comb % 8)
    p += 2
  elif op == 6:
    b = int(a/(2**comb))
    p += 2
  elif op == 7:
    c = int(a/(2**comb))
    p += 2


# ans
ans = ""
for num in out:
  ans += str(num) + ","
ans = ans[:-1]
print(ans)
