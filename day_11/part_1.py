# stones = [int(stone)
#           for stone in open("sample.txt", "r").read()[:-1].split(" ")]
stones = [int(stone)
          for stone in open("input.txt", "r").read()[:-1].split(" ")]


# BLINKS = 6
BLINKS = 25

for blink in range(BLINKS):
  new_stones = []
  for stone in stones:
    if stone == 0:
      new_stones.append(1)
    elif len(str(stone)) & 1 == 0:
      stone_len = len(str(stone))
      new_stones.append(int(str(stone)[:stone_len//2]))
      new_stones.append(int(str(stone)[stone_len//2:]))
    else:
      new_stones.append(stone*2024)

  stones = new_stones

print(len(new_stones))
