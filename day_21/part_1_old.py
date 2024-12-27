from collections import defaultdict
codes = open("sample.txt", "r").read().split("\n")[:-1]
# codes = open("input.txt", "r").read().split("\n")[:-1]

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
ngap = 2

# left and down is positive
dirs = {
    "A": 0,
    "^": 1,
    ">": 1j,
    "v": 1j + 1,
    "<": 1j + 2
}
dgap = 2


# generate all best dir pairs
dir_pairs = defaultdict(list)
for c1 in "<v^>A":
  for c2 in "<v^>A":
    if c1 == c2:
      dir_pairs[(c1, c2)] = ["A"]
      continue
    pos = dirs[c1]
    npos = dirs[c2]
    best = []
    if npos.real - pos.real < 0:
      for i in range(abs(int(npos.real - pos.real))):
        pos += 1
        best.append(">")
    if npos.imag - pos.imag > 0:
      for i in range(abs(int(npos.imag - pos.imag))):
        pos -= 1j
        if pos == dgap:
          pos -= 1
          best.append(">")

        best.append("^")

    if npos.imag - pos.imag < 0:
      for i in range(abs(int(npos.imag - pos.imag))):
        pos += 1j
        best.append("v")

    if npos.real - pos.real > 0:
      for i in range(abs(int(npos.real - pos.real))):
        pos -= 1
        best.append("<")
      # press button
    best.append("A")
    dir_pairs[(c1, c2)] = best

# generate all best numeric pairs
numeric_pairs = defaultdict(list)
for c1 in "7894561230A":
  for c2 in "7894561230A":
    if c1 == c2:
      numeric_pairs[(c1, c2)] = ["A"]
      continue

    pos = numeric[c1]
    npos = numeric[c2]
    change = npos - pos
    best = []
    if npos.imag - pos.imag > 0:
      for i in range(abs(int(npos.imag - pos.imag))):
        pos -= 1j
        best.append("^")

    if npos.real - pos.real < 0:
      for i in range(abs(int(npos.real - pos.real))):
        pos += 1
        best.append(">")

    if npos.imag - pos.imag < 0:
      for i in range(abs(int(npos.imag - pos.imag))):
        pos += 1j
        if pos == ngap:
          pos -= 1
          best.append(">")
        best.append("v")

    if npos.real - pos.real > 0:
      for i in range(abs(int(npos.real - pos.real))):
        pos -= 1
        best.append("<")
      # press button
    best.append("A")
    numeric_pairs[(c1, c2)] = best


total = 0
DIR_NUM = 2
for code in codes:
  num = int(code[:-1])
  new_code = []
  # start at A
  cur = "A"
  # numeric first
  for c in code:
    for dir in numeric_pairs[(cur, c)]:
      new_code.append(dir)
    cur = c
  code = new_code

  for j in range(DIR_NUM):
    cur = "A"
    new_code = []
    for c in code:
      for dir in dir_pairs[(cur, c)]:
        new_code.append(dir)
      cur = c
    code = new_code
  # print(code)
  print(len(code), num)
  total += len(code) * num

print(total)
