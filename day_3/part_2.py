import re

string = open("input.txt", "r").read()[:-1]

def match_mut(string):
  return re.findall(r"mul\(\d+,\d+\)", string)

def parse_mult(instr):
  nums = tuple(map(int, instr[4:-1].split(",")))
  return nums[0] * nums[1]

total = 0

split_dont = string.split("don't()")[1:]
for donts in split_dont:
  dos_donts = donts.split("do()")
  # only first dont, rest do
  for i in range(1, len(dos_donts)):
    for match in match_mut(dos_donts[i]):
      total += parse_mult(match)

# edge case parse the parts before the first dont
for match in match_mut(string.split("don't()")[0]):
  total += parse_mult(match)

print(total)

