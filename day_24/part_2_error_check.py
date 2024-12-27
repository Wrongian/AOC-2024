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

op_dict = defaultdict(list)
todo = deque([])

max_z = 0
ops = {}
for op_raw in ops_raw.split("\n"):
  op_str, out = op_raw.split(" -> ")
  w1, op, w2 = op_str.split(" ")

  # get the max z val
  if out[0] == "z":
    new_z = int(out[1:])
    max_z = max(max_z, new_z)

  if w1 not in wires or w2 not in wires:
    op_dict[w1].append((w1, op, w2, out))
    op_dict[w2].append((w1, op, w2, out))
    ops[(w1, op, w2)] = out
  else:
    todo.append((w1, op, w2, out))


y = []
y_val = max_y
while y_val >= 0:
  wy = "y"
  if y_val < 10:
    wy += "0"
  wy += str(y_val)
  y.append(wires[wy])
  y_val -= 1

y = y[::-1]

x = []
x_val = max_x
while x_val >= 0:
  wx = "x"
  if x_val < 10:
    wx += "0"
  wx += str(x_val)
  x.append(wires[wx])
  x_val -= 1
x = x[::-1]

# correct carries and sums
carries = []
sums = []
val = 0
carry = 0
while val <= max_x:
  s = (x[val] ^ y[val]) ^ carry
  carry = ((x[val] ^ y[val]) & carry) | (x[val] & y[val])
  sums.append(s)
  carries.append(carry)
  val += 1

if carry != 0:
  sums.append(carry)

"""
inputs should follow(including order of operations) for n >= 1
(xn xor yn) xor carry
((xn xor yn) and carry) or (xn and yn)
full adder

"""

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

z = []
z_val = max_z
while z_val >= 0:
  wz = "z"
  if z_val < 10:
    wz += "0"
  wz += str(z_val)
  z.append(wires[wz])
  z_val -= 1

z = z[::-1]

# find out which digits are wrong and manually check
wrong = []
for i, z_digit in enumerate(z):
  if z_digit != sums[i]:
    wrong.append(i)

print(wrong)
