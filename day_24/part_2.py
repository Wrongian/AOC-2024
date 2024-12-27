import graphviz

# ws_raw, ops_raw = open("sample.txt", "r").read()[:-1].split("\n\n")
ws_raw, ops_raw = open("input.txt", "r").read()[:-1].split("\n\n")

max_x = 0
max_y = 0


f = graphviz.Digraph('Gates', filename='gates.gv')
f.attr(rankdir='LR', size='100,100')
f.attr('node', shape='circle')

ops = {}
for op_raw in ops_raw.split("\n"):
  op_str, out = op_raw.split(" -> ")
  w1, op, w2 = op_str.split(" ")

  f.edge(w1, out, label=op)
  f.edge(w2, out, label=op)

f.view()
