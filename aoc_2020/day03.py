from utils import loadInput, loadeg, grid
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()
pairs = ((1,1),(3,1),(5,1),(7,1),(1,2))
# width 10
# 0 - 9 index 10 - 19 inclusive is next group % 10
g = grid(inputLines)
print(g)
h,w = len(g), len(g[0])
xcor,ycor = 0,0
print(g[2][6])
trees = []
for r,d in pairs:
    t = 0
    xcor,ycor = 0,0
    while (ycor < h):
        item = g[ycor][xcor]
        t = t + 1 if item == '#' else t
        xcor = (xcor + r) % w
        ycor = (ycor + d)
        # print(xcor, ycor)
    print(t)
    trees.append(t)
print(np.prod(trees))