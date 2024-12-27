from sympy import solve
from sympy.abc import a, b

"""
solve the equations for least a,b such that
ax_1 + 3bx_2 = 3x_3
ay_1 + 3by_2 = 3y_3
alternatively can use cramers rule, or whatever other algorithms that solve linear eqns
or just manually find formula for eqn
or just use formula for inverse mat
"""

# machines_str = open("sample.txt", "r").read()[:-1].split("\n\n")
machines_str = open("input.txt", "r").read()[:-1].split("\n\n")

total = 0
for machine_str in machines_str:
  split_str = machine_str.split("\n")
  # probably use regex next time :3
  _, _2, ax_str, ay_str = split_str[0].split(" ")
  ax_str = ax_str[:-1]
  ax = int(ax_str[2:])
  ay = int(ay_str[2:])

  _, _2, bx_str, by_str = split_str[1].split(" ")
  bx_str = bx_str[:-1]
  bx = int(bx_str[2:])*3
  by = int(by_str[2:])*3

  _, px_str, py_str = split_str[2].split(" ")
  px_str = px_str[:-1]
  px = (int(px_str[2:]) + 10000000000000) * 3
  py = (int(py_str[2:]) + 10000000000000) * 3

  # get all solns to simult eqns
  solns = solve([ax*a + bx*b - px, ay*a + by*b - py], [a, b], dict=True)
  min_tokens = float("inf")
  # should only have 1 soln or 0(assume no infinite) anyway
  for soln in solns:
    if not (soln[a]/3).is_integer:
      continue
    if not soln[b].is_integer:
      continue

    tokens = int(soln[a] + soln[b])

    min_tokens = min(min_tokens, tokens)

  if min_tokens == float("inf"):
    continue
  total += min_tokens

print(total)
