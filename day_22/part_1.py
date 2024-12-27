# nums = list(map(int, open("sample.txt", "r").read().split("\n")[:-1]))
nums = list(map(int, open("input.txt", "r").read().split("\n")[:-1]))
# nums = [123]

# iterations = 10
ITERATIONS = 2000
total = 0
for num in nums:
  n = num
  for i in range(ITERATIONS):
    nn = n
    nn = ((nn*64) ^ nn) % 16777216
    nn = ((nn//32) ^ nn) % 16777216
    nn = ((nn*2048) ^ nn) % 16777216
    n = nn

  total += n

print(total)
