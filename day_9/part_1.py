# line = open("sample.txt", "r").read()[:-1]
line = open("input.txt", "r").read()[:-1]

# generate disc
disc = []
id = 0
for i, c in enumerate(line):
  num = int(c)
  # odd free
  if i & 1:
    for j in range(num):
      # -1 for free space
      disc.append(-1)
  # even
  else:
    for j in range(num):
      disc.append(id)
    id += 1

# sliding window
left = 0
right = len(disc) - 1

while left < right:
  # move window
  if disc[left] != -1:
    left += 1
    continue
  if disc[right] == -1:
    right -= 1
    continue

  # if both blank then switch
  disc[left], disc[right] = disc[right], disc[left]
  left += 1
  right -= 1

# calc checksum
checksum = 0
for i, num in enumerate(disc):
  # if encounter end
  if num == -1:
    break
  checksum += num * i

print(checksum)
