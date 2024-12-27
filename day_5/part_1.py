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

  is_correct = True
  done = set()

  for num in page:
    num_depen = []
    for depen in depens:
      if depen[1] == num and depen[0] in done:
        is_correct = False

    done.add(num)

  if is_correct: 
    # assume all pages are odd
    total += page[len(page)//2]

print(total)

