# nums = list(map(int, open("sample.txt", "r").read().split("\n")[:-1]))
nums = list(map(int, open("input.txt", "r").read().split("\n")[:-1]))
# nums = [123]

# iterations = 10
ITERATIONS = 2000
total = 0
changes_set = set()
ones_dict = {}
for num in nums:
  n = num
  changes = []
  ones_dict[num] = {}
  for i in range(ITERATIONS):
    nn = n
    nn = ((nn*64) ^ nn) % 16777216
    nn = ((nn//32) ^ nn) % 16777216
    nn = ((nn*2048) ^ nn) % 16777216
    n_one = int(str(n)[-1])
    nn_one = int(str(nn)[-1])
    c = nn_one - n_one
    if len(changes) < 3:
      changes.append(c)
    elif len(changes) == 3:
      changes.append(c)
      tup_changes = tuple(changes)
      if tup_changes not in ones_dict[num]:
        changes_set.add(tup_changes)
        ones_dict[num][tup_changes] = nn_one
    else:
      changes.pop(0)
      changes.append(c)
      tup_changes = tuple(changes)
      if tup_changes not in ones_dict[num]:
        changes_set.add(tup_changes)
        ones_dict[num][tup_changes] = nn_one
    n = nn


best = 0
for c in changes_set:
  total = 0
  for num in nums:
    if num in ones_dict and c in ones_dict[num]:
      total += ones_dict[num][c]
  best = max(best, total)

print(best)
