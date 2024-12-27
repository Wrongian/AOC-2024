# stones = [int(stone)
#           for stone in open("sample.txt", "r").read()[:-1].split(" ")]
stones = [int(stone)
          for stone in open("input.txt", "r").read()[:-1].split(" ")]


# BLINKS = 6
BLINKS = 75

dp = {}


def dfs(stone, blinks):

  # termination cond
  if blinks == 0:
    return 1

  if (stone, blinks) in dp:
    return dp[(stone, blinks)]

  if stone == 0:
    total_len = dfs(1, blinks - 1)
  elif len(str(stone)) & 1 == 0:
    stone_len = len(str(stone))
    total_len = dfs(int(str(stone)[:stone_len//2]), blinks - 1) + \
        dfs(int(str(stone)[stone_len//2:]), blinks - 1)
  else:
    total_len = dfs(stone*2024, blinks - 1)

  dp[(stone, blinks)] = total_len

  return total_len


total_len = 0
for stone in stones:
  total_len += dfs(stone, BLINKS)

print(total_len)
