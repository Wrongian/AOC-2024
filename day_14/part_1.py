# robots = open("sample.txt", "r").read().split("\n")[:-1]
robots = open("input.txt", "r").read().split("\n")[:-1]

# sample
# mx = 11
# my = 7

# input
mx = 101
my = 103

SECS = 100

q1, q2, q3, q4 = 0, 0, 0, 0


def add_quad(x, y):
  global q1, q2, q3, q4
  mid_x = mx//2
  mid_y = my//2

  if x < mid_x and y < mid_y:
    q1 += 1
  elif x > mid_x and y < mid_y:
    q2 += 1
  elif x < mid_x and y > mid_y:
    q3 += 1
  elif x > mid_x and y > mid_y:
    q4 += 1


for robot in robots:
  r_pos, r_vel = robot.split(" ")
  r_pos = r_pos[2:]
  r_vel = r_vel[2:]

  rx, ry = map(int, r_pos.split(","))
  vx, vy = map(int, r_vel.split(","))

  for sec in range(SECS):
    rx += vx
    rx %= mx
    ry += vy
    ry %= my

  add_quad(rx, ry)


# total safety
safety = q1*q2*q3*q4

# print(q1, q2, q3, q4)
print(safety)
