from utils import loadInput, loadeg, grid
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys
import copy

inputLines = loadInput()
# inputLines = loadeg()

# part 2 only
g = grid(inputLines)
h,w = len(g), len(g[0])

def adj_empty(y, x):
    for m in range(-1,2):
        for n in range(-1,2):
            t1,t2 = y,x
            while True:
                if (t1 + m >= h or t1 + m < 0 or t2 + n >= w or t2 + n < 0 or n == 0 and m == 0):
                    break
                r = g[t1 + m][t2 + n]
                if r == ".":
                    t1 += m
                    t2 += n
                elif r == "#":
                    return False
                elif r == 'L':
                    break
                # print(t1,t2,m,n)
    return True
                
def adj_five_occ(y, x):
    c = 0
    for m in range(-1,2):
        for n in range(-1,2):
            t1,t2 = y,x
            while True:
                if (t1 + m >= h or t1 + m < 0 or t2 + n >= w or t2 + n < 0 or n == 0 and m == 0):
                    break
                r = g[t1 + m][t2 + n]
                if r == ".":
                    t1 += m
                    t2 += n
                elif r == "#":
                    c += 1
                    if c == 5:
                        return True
                    break
                elif r == 'L':
                    break
    return False


c = True
r = 0
while c:
    dc = copy.deepcopy(g)
    c = False
    for y in range(0, h):
        for x in range(0, w):
            s = g[y][x] # g[h][w]
            if s == 'L' and adj_empty(y, x):
                dc[y][x] = '#'
                c = True
            elif s == '#' and adj_five_occ(y, x):
                dc[y][x] = 'L'
                c = True
            else:
                continue
    # print(dc)
    g = dc
    r += 1
print(sum([g[y][x] == '#' for y in range(0,h) for x in range(0, w)]))
print("constant state")
print(r)