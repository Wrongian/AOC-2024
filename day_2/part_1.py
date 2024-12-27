lines = open("input.txt", "r").readlines()

total = 0
for line in lines:
  nums = tuple(map(int, line[:-1].split(" ")))
  new_nums = [(nums[i - 1] - nums[i]) > 0 for i in range(1, len(nums))]
  # check if increasing or decreasing
  is_safe = all(new_nums) | (not any(new_nums))
  # check if at least one and at most three
  new_nums = [abs(nums[i - 1] - nums[i]) >= 1 and abs(nums[i - 1] - nums[i]) <= 3 for i in range(1, len(nums))]
  is_safe = is_safe & all(new_nums)
  if is_safe:
    total += 1
print(total)

  