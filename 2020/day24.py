from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys
import copy

inputLines = loadInput()
inputLines = loadeg()

m = {}
for l in inputLines:
    i = 0
    x,y = 0,0
    while i < len(l):
        c = l[i]
        match c:
            case "e":
                x += 1
            case "w":
                x -= 1
            case "s":
                dir = l[i+1]
                y -= 1
                x = x - 0.5 if dir == "w" else x + 0.5
                i += 1
            case "n":
                dir = l[i+1]
                y += 1
                x = x - 0.5 if dir == "w" else x + 0.5
                i += 1
        i += 1
    if (x,y) in m:
        m[(x,y)] = (m[(x,y)] + 1) % 2
    else:
        m[(x,y)] = 1 # flipped to black

# m = {(0,0) : 0}
adj = [(-0.5,0),(-0.5,-1),(0.5,-1),(0.5,0),(0.5,1),(-0.5,1)]
keys = frozenset(m.keys())
for (x,y) in keys:
    for (a,b) in adj:
        if (x+a,y+b) not in m:
            m[(x+a,y+b)] = 0
# print(sum(list(m.values())))
for r in range(1):
    keys = frozenset(m.keys())
    for (x,y) in keys:
        for (a,b) in adj:
            if (x+a,y+b) not in m:
                m[(x+a,y+b)] = 0
    temp_m = copy.deepcopy(m)
    print(m)
    for ((x,y), v) in m.items():
        black_adj = sum([m[(x+a, y+b)] == 1 if (x+a, y+b) in m else 0 for (a,b) in adj])
        # black_adj_tiles = [((x+a, y+b),m[(x+a, y+b)]) for (a,b) in adj if (x+a, y+b) in m ]
        # print(black_adj_tiles)
        if v == 1:
            if black_adj == 0 or black_adj >= 2:
                print("flipping to white", ((x,y),v))
                temp_m[(x,y)] = 0
        else:
            # white
            if black_adj == 2:
                print("flipping to black", ((x,y),v)) 
                temp_m[(x,y)] = 1

    m = temp_m
    
print(m)
print(sum(list(m.values())))
    