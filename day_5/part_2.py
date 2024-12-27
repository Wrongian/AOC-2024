# depens_raw, pages_raw = open("sample.txt", "r").read().split("\n\n")
depens_raw, pages_raw = open("input.txt", "r").read().split("\n\n")

depens_txt = [depen.split("\\") for depen in depens_raw.split("\n")]
depens = [] 
for depen_txt in depens_txt:
  depen = depen_txt[0].split("|")
  depens.append((int(depen[1]),int(depen[0])))

pages = [list(map(int, page.split(","))) for page in pages_raw.split("\n")[:-1]]

total = 0
# verify each page
for page in pages:

  done = set()
  is_correct = True
  new_order = []

  for num in page:
    to_add = []
    for depen in depens:
      if depen[1] == num and depen[0] in done:
        is_correct = False
        # assume no dupes
        ind = new_order.index(depen[0])
        to_add.append((ind,depen[0]))

    to_add.sort()

    for ind, add_num in to_add:
      new_order.remove(add_num)
      new_order.append(add_num)

    done.add(num)

  # assume all pages are odd
  if is_correct == False:
    total += new_order[len(page)//2]


print(total)

