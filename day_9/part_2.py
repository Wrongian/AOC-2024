# line = open("sample.txt", "r").read()[:-1]
line = open("input.txt", "r").read()[:-1]


class Node():
  def __init__(self, size, id):
    self.size = size
    self.next = None
    self.prev = None
    # -1 for free
    self.id = id


# generate linked list disc
id = 0
cur_node = Node(0, -1)
start_node = cur_node

for i, c in enumerate(line):
  num = int(c)
  new_node = None

  # odd free
  if i & 1:
    # -1 for free space
    new_node = Node(num, -1)

  # even
  else:
    new_node = Node(num, id)
    id += 1

  cur_node.next = new_node
  new_node.prev = cur_node
  cur_node = new_node

start_node = start_node.next

# move disc
right_node = cur_node

while right_node != start_node:
  while right_node.id == -1:
    right_node = right_node.prev

  needed_space = right_node.size
  left_node = start_node

  # find suitable space
  while left_node != right_node and (left_node.id != -1 or left_node.size < needed_space):
    left_node = left_node.next

  # no suitable space found
  if left_node == right_node:
    right_node = right_node.prev
    continue

  # replace the space
  # replace 1 node
  if needed_space == left_node.size:
    left_node.id = right_node.id
    right_node.id = -1
  # replace 1 and create 1 node
  else:
    # change ids
    left_node.id = right_node.id
    right_node.id = -1

    # change space
    # free space
    new_node = Node(left_node.size - needed_space, -1)
    # left node
    left_node.size = needed_space

    # change linked list
    saved_next = left_node.next
    left_node.next = new_node
    new_node.prev = left_node
    new_node.next = saved_next
    saved_next.prev = new_node

  right_node = right_node.prev

# calc checksum
checksum = 0
node = start_node
ind = 0

while node != None:
  # print(str(node.id) * node.size, end="")

  if node.id == -1:
    ind += node.size
    node = node.next
    continue

  for i in range(node.size):
    checksum += node.id * (ind+i)

  ind += node.size
  node = node.next

# print("")
print(checksum)
