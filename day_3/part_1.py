import re

string = open("input.txt", "r").read()[:-1]

matches = re.findall(r"mul\(\d+,\d+\)", string)

total = 0
for match in matches:
  nums = tuple(map(int, match[4:-1].split(",")))
  total += nums[0] * nums[1]

print(total)

