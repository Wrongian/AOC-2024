inp = open("input.txt", "r").readlines()

nums = [tuple(map(int,line[:-1].split("   "))) for line in inp]
num_1 = sorted([tup[0] for tup in nums])
num_2 = sorted([tup[1] for tup in nums])

total = 0

for i in range(len(num_1)):
  total += abs(num_1[i] - num_2[i])

print(total)