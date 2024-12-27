lines = open("input.txt", "r").readlines()

total = 0

def check_safe(nums):
  new_nums = [(nums[i - 1] - nums[i]) > 0 for i in range(1, len(nums))]
  # check if increasing or decreasing
  is_safe = all(new_nums) | (not any(new_nums))
  # check if at least one and at most three
  new_nums = [abs(nums[i - 1] - nums[i]) >= 1 and abs(nums[i - 1] - nums[i]) <= 3 for i in range(1, len(nums))]
  is_safe = is_safe & all(new_nums)
  return is_safe

for line in lines:
  nums = tuple(map(int, line[:-1].split(" ")))
  is_safe = check_safe(nums)
  if is_safe:
    total += 1
  else:
    # check if can remove 1
    for i in range(len(nums)):
      new_nums = nums[:i] + nums[i + 1:]
      if check_safe(new_nums):
        total += 1
        break

print(total)

  