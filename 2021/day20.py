from utils import loadInput, loadeg, grid
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys
import copy

inputLines = loadInput()
# inputLines = loadeg()

algo = inputLines[0]
# g = grid(inputLines[2:])
print(inputLines)
i = 0
t = []
while (i < len(inputLines)):
    line = inputLines[i]
    t += inputLines[i]
    if line == "":
        i += 1
        break
    i += 1
# works for main input only
# t = inputLines[0]
g = grid(inputLines[i:])
print(t)
print(g)

def surround(y, x):
    return [(y + m, x + n) for (m,n) in \
        [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]]

inf = "." # keep track of the infite value
m = {}
for y in range(len(g)):
    for x in range(len(g[0])):
        m[(y,x)] = g[y][x]
        if y == 0 or y == len(g) - 1 or x == 0 or x == len(g[0]) - 1:
            pixels = surround(y,x)
            for (a,b) in pixels:
                if a < 0 or a >= len(g) or b < 0 or b >= len(g[0]):
                    # print("setting", (a,b), inf)
                    m[(a,b)] = inf
m2 = {}
count = sum([v == "#" for k,v in m.items()])
print("count: ", count)
print(len(m))
for step in range(50):
    m2.clear()
    for (y,x) in m.keys():
        pixels = surround(y, x)
        # print(pixels)
        row = []
        updated_inf = t[(0 if inf == "." else -1)]
        # print(updated_inf)
        for (a,b) in pixels:
            if (a,b) not in m:
                row.append(inf)
                m2[(a,b)] = updated_inf
            else:
                row.append(m[(a,b)])
        bits = "".join(['0' if x == "." else '1' for x in row])
        binary = int(bits, 2)
        output = t[binary]
        # update the next generation
        m2[(y,x)] = output
        
    inf = updated_inf
        # print((y,x), bits, binary, output)
    print(inf)
    m = copy.deepcopy(m2)
        
    count = sum([v == "#" for k,v in m.items()])
    print("count: ", count)
            
# for step in range(2):
    
        
# print(algo, grid)