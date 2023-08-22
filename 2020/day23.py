from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import math
import sys
import copy

inputLines = loadInput()
inputLines = loadeg()
m = {}
f = defaultdict(int)
f_once = 0
f_twice = 0
f_three = 0
print(len(inputLines))
for l in inputLines:
    i = 0
    x,y = 0,0
    while i < len(l):
        c = l[i]
        if c == "e":
            x += 1
        elif c == "w":
            x -= 1
        elif c == "n":
            y += 1
            if l[i + 1] == "e":
                x += 0.5
            else:
                x -= 0.5
            i += 1
        elif c == "s":
            y -= 1
            if l[i + 1] == "e":
                x += 0.5
            else:
                x -= 0.5
            i += 1
        i += 1
    if (x,y) in m:
        m[(x,y)] = (m[(x,y)] + 1) % 2
    else:
        m[(x,y)] = 1 # to black
    f[(x,y)] += 1
# print(*f.items(), sep="\n")
for (k, v) in m.items():
    if v == 1:
        print(k,v)

adj = [(-1,0),(-0.5,-1),(0.5,-1),(1,0),(0.5,1),(-0.5,1)]
# set white tiles in range that aren't listed

# IMPROVE OPTIMISATION
print(sum(m.values()))
for r in range(100):
    # print(m)
    to_flip = set()
    orig_keys = frozenset(m.items())
    checked = set()
    for ((x,y),v) in orig_keys:
        if v == 1:
            need_to_check = {(x+a,y+b) for (a,b) in adj}
            need_to_check.add((x,y))
            left_to_check = need_to_check.difference(checked)
            checked = checked.union(left_to_check)
        else:
            continue
        for (i,j) in left_to_check:
            sum_adj = sum([m[(i+a,j+b)] == 1 for (a,b) in adj if (i+a,j+b) in m])
            if (i,j) in m and m[(i,j)] == 1:
                if sum_adj == 0 or sum_adj > 2:
                    to_flip.add((i,j))
            else:
                if sum_adj == 2:
                    to_flip.add((i,j))
    for (x,y) in to_flip:
        if (x,y) in m:
            m[(x,y)] = (m[(x,y)] + 1) % 2
        else:
            m[(x,y)] = 1
# print("\n")
# print(*m.items(), sep="\n")
print(sum(m.values()))