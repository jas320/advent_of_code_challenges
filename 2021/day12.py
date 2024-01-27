from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()

print("hello world")

m = defaultdict(list)

for l in inputLines:
    a,b = l.split("-")
    m[a].append(b)
    m[b].append(a)
startl = m["start"]
print(m)

m2 = defaultdict(int)
# recursive
def dfs(curr, path, sc):
    c = 0
    if curr == "start" and len(path) > 0:
        return 0
    if curr == "end":
        return 1
    else:
        ns = m[curr] if curr in m else []
        for node in ns:
            if (node not in path and node != sc) or node.isupper() or (node == sc and m2[sc] < 2):
                if node == sc:
                    m2[sc] += 1
                elif node.islower():
                    path.add(node)
                c += dfs(node, path, sc)
                if node == sc:
                    m2[sc] -= 1
                elif node.islower():
                    path.remove(node)
        return c
mv = -1
print(m.keys())
base = dfs("start", set(), "")
t = 0
print(base)
for n in m.keys():
    if n[0].islower() and n != "start" and n != "end":
        nv = dfs("start", set(), n)
        t += (nv - base)
print(t + base)
# print(mv)

# mv = -9
# for n in m.keys():
#     mv = max(mv, dfs("start", set(), n))
    
