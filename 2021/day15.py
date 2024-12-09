from utils import loadInput, loadeg, grid
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys
from heapdict import heapdict

inputLines = loadInput()
# inputLines = loadeg()

def neighbors(t):
    y, x = t
    return [(y + m, x + n) for (m,n) in [(-1,0), (1,0), (0,-1),(0,1)] if 0 <= (y + m) < len(g) and 0 <= (x + n) < len(g[0])]

g = grid(inputLines)
for y in range(len(g)):
    for x in range(len(g[0])):
        g[y][x] = int(g[y][x])
fixed = len(g[0])
for y in range(len(g)):
    line = g[y]
    temp = []
    for c in range(1,5):
        temp.append([g[y][x] + c if g[y][x] + c < 10 else g[y][x] + c - 9 for x in range(fixed)])
        # print(temp)
        c += 1
    for ls in temp:
        line.extend(ls)
    g[y] = line
    # print(y, g[y])
fixed_x = len(g[0])
fixed_y = len(g)
print(len(g) - 1, len(g[0]) - 1)
for j in range(1,5):
    next = []
    for y in range(len(g) - fixed_y, len(g)):
        last = g[y][-fixed_x: ]
        new = [x + 1 if x + 1 < 10 else x + 1 - 9 for x in last]
        new_list = g[y][fixed_x:] + new
        g.append(new_list)
        # print(y, new_list)
    # print("\n")
for y in range(len(g)):
    # print(y, g[y])
    pass
        
        
    
# print(g)
start = (0, 0)
end = (len(g) - 1, len(g[0]) - 1)
print(len(g) - 1, len(g[0]) - 1)

# map m is the tentative distance is shortest path from node v to the starting node.

coordinates = {(a,b) for a in range(len(g)) for b in range(len(g[0]))}
curr = start
h = heapdict()
for x in coordinates:
    h[x] = float('inf')
final = {}
h[curr] = 0
while len(h) > 0:
    final[curr] = h[curr]
    ns = neighbors(curr)
    for node in ns:
        if node in h:
            y, x = node
            total_dist = h[curr] + g[y][x]
            if total_dist < h[node]:
                h[node] = total_dist
    h[curr] = -1
    h.popitem()
    if len(h) == 0:
        break
    (curr, curr_distance) = h.peekitem()
    if (end in final): # or curr_distance == "final" second clause implies disconnected graph (unreachable)
        break
# print(final)
# print(g[0])
print(final[end])
# print(final)
# print(visited)
        
                
