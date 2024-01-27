from utils import loadInput, loadeg, grid
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()

g = grid(inputLines)
for y in range(len(g)):
    g[y] = list(map(int,g[y]))
print(g)
flashed = set()
c = 0
all = len(g) * len(g[0])
for i in range(1,1000):
    flashed.clear()
    # print("after step", i)
    for y in range(len(g)):
        for x in range(len(g[0])):
            g[y][x] += 1
            if (y,x) not in flashed:
                if g[y][x] > 9:
                    flashed.add((y,x))
                    stack = [(y,x)]
                    while stack:
                        m,n = stack.pop()
                        ns = [(m - 1, n - 1),(m, n - 1),(m - 1,n),(m+1,n),(m,n+1),(m - 1,n+1),(m+1,n-1),(m+1,n+1)]
                        for (a,b) in ns:
                            if 0 <= a < len(g) and 0 <= b < len(g[0]):
                                g[a][b] += 1
                                if (a,b) not in flashed and g[a][b] > 9:
                                    stack.append((a,b))
                                    flashed.add((a,b))
    if len(flashed) == all:
        print(i)
        quit()
    for (y,x) in flashed:
        g[y][x] = 0
        c += 1
    # print("after step", i)
    # for y in range(len(g)):
    #     print(g[y])
print(c)

                