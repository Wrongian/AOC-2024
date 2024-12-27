from itertools import permutations
from copy import deepcopy
from collections import deque
from collections import defaultdict
# ws_raw, ops_raw = open("sample.txt", "r").read()[:-1].split("\n\n")
ws_raw, ops_raw = open("input.txt", "r").read()[:-1].split("\n\n")

max_x = 0
max_y = 0

wires = {}
for ws in ws_raw.split("\n"):
  ws_name, val = ws.split(": ")
  wires[ws_name] = int(val)

  # max x and y
  if ws_name[0] == "x":
    new_x = int(ws_name[1:])
    max_x = max(new_x, max_x)
  if ws_name[0] == "y":
    new_y = int(ws_name[1:])
    max_y = max(new_y, max_y)

# depended_on = defaultdict(list)
op_dict = defaultdict(list)
todo_ori = deque([])

max_z = 0
for op_raw in ops_raw.split("\n"):
  op_str, out = op_raw.split(" -> ")
  w1, op, w2 = op_str.split(" ")

  # get the max z val
  if out[0] == "z":
    new_z = int(out[1:])
    max_z = max(max_z, new_z)

  if w1 not in wires or w2 not in wires:
    # depended_on[w1].append(out)
    # depended_on[w2].append(out)
    op_dict[w1].append((w1, op, w2, out))
    op_dict[w2].append((w1, op, w2, out))
  else:
    todo_ori.append((w1, op, w2, out))


y = 0
y_val = max_y
while y_val >= 0:
  wy = "y"
  if y_val < 10:
    wy += "0"
  wy += str(y_val)
  y <<= 1
  y += wires[wy]
  y_val -= 1

x = 0
x_val = max_x
while x_val >= 0:
  wx = "x"
  if x_val < 10:
    wx += "0"
  wx += str(x_val)
  x <<= 1
  x += wires[wx]
  x_val -= 1

# get all permutations of 8
for permute in permutations(op_dict.keys()):
  p_list = list(permute)
  todo = todo_ori.copy()

  # swap dictionary
  op_dict[p_list[0]], op_dict[p_list[1]
                              ] = op_dict[p_list[1]], op_dict[p_list[0]]
  op_dict[p_list[2]], op_dict[p_list[3]
                              ] = op_dict[p_list[4]], op_dict[p_list[3]]
  op_dict[p_list[4]], op_dict[p_list[5]
                              ] = op_dict[p_list[5]], op_dict[p_list[4]]
  op_dict[p_list[6]], op_dict[p_list[7]
                              ] = op_dict[p_list[7]], op_dict[p_list[6]]

  while todo:
    # do the op
    w1, op, w2, out = todo.popleft()
    if op == "AND":
      wires[out] = wires[w1] & wires[w2]
    elif op == "OR":
      wires[out] = wires[w1] | wires[w2]
    elif op == "XOR":
      wires[out] = wires[w1] ^ wires[w2]
    else:
      raise ValueError("Unknown op")
    for nw1, nop, nw2, nout in op_dict[out]:
      # wait till both operands in first
      if nw1 not in wires or nw2 not in wires:
        continue
      todo.append((nw1, nop, nw2, nout))

  z = 0
  z_val = max_z
  while z_val >= 0:
    wz = "z"
    if z_val < 10:
      wz += "0"
    wz += str(z_val)
    z <<= 1
    z += wires[wz]
    z_val -= 1

  # swap dictionary
  op_dict[p_list[0]], op_dict[p_list[1]
                              ] = op_dict[p_list[1]], op_dict[p_list[0]]
  op_dict[p_list[2]], op_dict[p_list[3]
                              ] = op_dict[p_list[4]], op_dict[p_list[3]]
  op_dict[p_list[4]], op_dict[p_list[5]
                              ] = op_dict[p_list[5]], op_dict[p_list[4]]
  op_dict[p_list[6]], op_dict[p_list[7]
                              ] = op_dict[p_list[7]], op_dict[p_list[6]]
  if y + x == z:
    print(",".join(sorted(p_list)))
    break
