from collections import deque
from collections import defaultdict
# ws_raw, ops_raw = open("sample.txt", "r").read()[:-1].split("\n\n")
ws_raw, ops_raw = open("input.txt", "r").read()[:-1].split("\n\n")

wires = {}
for ws in ws_raw.split("\n"):
  ws_name, val = ws.split(": ")
  wires[ws_name] = int(val)

op_dict = defaultdict(list)
todo = deque([])

for op_raw in ops_raw.split("\n"):
  op_str, out = op_raw.split(" -> ")
  w1, op, w2 = op_str.split(" ")
  if w1 not in wires or w2 not in wires:
    op_dict[w1].append((w1, op, w2, out))
    op_dict[w2].append((w1, op, w2, out))
  else:
    todo.append((w1, op, w2, out))

max_z = 0
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
  # get the max z val
  if out[0] == "z":
    new_z = int(out[1:])
    max_z = max(max_z, new_z)


num = 0
z_val = max_z
while z_val >= 0:
  wz = "z"
  if z_val < 10:
    wz += "0"
  wz += str(z_val)
  num <<= 1
  num += wires[wz]
  z_val -= 1

print(num)
