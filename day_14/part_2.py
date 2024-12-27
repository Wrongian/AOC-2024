from collections import defaultdict
# robots = open("sample.txt", "r").read().split("\n")[:-1]
robots = open("input.txt", "r").read().split("\n")[:-1]

# sample
# mx = 11
# my = 7

# input
mx = 101
my = 103


num_robots = 0
poses = []
vels = []
mid_x = mx//2
mid_y = my//2

q1, q2, q3, q4 = 0, 0, 0, 0
for robot in robots:
  r_pos, r_vel = robot.split(" ")
  r_pos = r_pos[2:]
  r_vel = r_vel[2:]

  rx, ry = map(int, r_pos.split(","))
  vx, vy = map(int, r_vel.split(","))

  poses.append([rx, ry])
  vels.append((vx, vy))

  if rx < mid_x and ry < mid_y:
    q1 += 1
  elif rx > mid_x and ry < mid_y:
    q2 += 1
  elif rx < mid_x and ry > mid_y:
    q3 += 1
  elif rx > mid_x and ry > mid_y:
    q4 += 1
  num_robots += 1


# "inverse density"
def calc_density():
  density = 0
  for x1, y1 in poses:
    for x2, y2 in poses:
      if x1 == x2 and y1 == y2:
        continue
      density += abs(x2-x1) + abs(y2-y1)
  return density
  # return (q1**2)*(q2**2)*(q3**2)*(q4**2)


densities = []
densities.append((calc_density(), 0))
SECS = 10000
for s in range(1, SECS+1):
  q1, q2, q3, q4 = 0, 0, 0, 0
  for i in range(num_robots):
    vx, vy = vels[i]
    poses[i][0], poses[i][1] = (poses[i][0] + vx) % mx, (poses[i][1] + vy) % my
    rx, ry = poses[i]

    if rx < mid_x and ry < mid_y:
      q1 += 1
    elif rx > mid_x and ry < mid_y:
      q2 += 1
    elif rx < mid_x and ry > mid_y:
      q3 += 1
    elif rx > mid_x and ry > mid_y:
      q4 += 1
  densities.append((calc_density(), s))


output = ""
robot_set = set(list(map(tuple, poses)))
# display tree
for y in range(my):
  for x in range(mx):
    if (x, y) in robot_set:
      output += "x"
    else:
      output += "."
  output += "\n"
open("out.txt", "w").write(output)

densities.sort()
print(densities[:4])
