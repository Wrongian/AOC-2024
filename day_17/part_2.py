# regs, instrs_raw = open("sample2.txt", "r").read()[:-1].split("\n\n")
regs, instrs_raw = open("input.txt", "r").read()[:-1].split("\n\n")
"""
formula here in text file to prevent input from being posted 
"""
formula = open("formula.txt", "r").read()

instrs = list(map(int, instrs_raw.split(": ")[1].split(",")))

"""
not monotonically increasing
a is very large(not brute forceable)

last op is a 3, 0 so jump to 0 if a not equals to 0
each time a is divided by 8(in my input) until 0
a/8 is a subproblem
b and c is determined by a at first and do some calculations
initial value of b and c doesnt matter
"""

contenders = [0]
while instrs:
  target_out = instrs.pop()
  new_contenders = []
  while contenders:
    contender = contenders.pop()
    for i in range(8):
      a = contender + i
      is_false = False
      out = eval(formula)
      if out == target_out:
        new_contenders.append(a*8)
  contenders = new_contenders

print(int(sorted(contenders)[0]/8))
