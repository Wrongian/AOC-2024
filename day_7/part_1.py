lines = open("input.txt", "r").read().split("\n")[:-1]
# lines = open("sample.txt", "r").read().split("\n")[:-1]

test_total = 0

for line in lines:
  nums_raw = line.split(" ")
  test_val = int(nums_raw[0][:-1])
  nums = list(map(int, nums_raw[1:]))

  seen = set()

  queue = []
  queue.append((nums[0], 1))

  while len(queue) > 0:
    total, ind = queue.pop(0)
    # seen before done before
    if (total, ind) in seen:
      continue
    seen.add((total, ind))

    # termination condition
    if ind >= len(nums):
      if total == test_val:
        test_total += test_val
        break
      continue

    # mult
    new_total = total * nums[ind]
    queue.append((new_total, ind + 1))

    # add
    new_total = total + nums[ind]
    queue.append((new_total, ind + 1))

print(test_total)
