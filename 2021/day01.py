from utils import loadInput, loadeg, grid
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()

def printf(g):
    print(" ", "".join(str(x) for x in list(range(len(g[0])))))
    for y in range(len(g)):
        print(y, "".join(g[y]))
        
g = grid(inputLines)
def get_lines(cors, t):
    oy, ox = t
    grads = defaultdict(list)
    first_hit = set()
    for pair in cors:
        y, x = pair
        if pair == t or g[y][x] != "#":
            continue
        if (x - ox) == 0:
            m = float('inf')
        else:
            m = (y - oy) / (x - ox)
        if x == ox:
            side = 4 if y > oy else 3
        else:
            side = 1 if x > ox else 0
        grads[(m ,side)].append((abs(oy - y) + abs(ox - x), (y, x), pair))
    [v.sort() for v in grads.values()]
    keys_3 = [(a,b) for (a,b) in grads.keys() if b == 3]
    keys_1 = [(a,b) for (a,b) in grads.keys() if b == 1]
    keys_0 = [(a,b) for (a,b) in grads.keys() if b == 0]
    keys_4 = [(a,b) for (a,b) in grads.keys() if b == 4]
    keys_0.sort()
    keys_1.sort()
    combined = keys_3 + keys_1 + keys_0 + keys_4
    c = 1
    print(combined)
    
    while c < 300:
        for k in combined:
            if len(grads[k]) > 0:
                popped = grads[k].pop(0)
                print(c, popped)
                c += 1
    return first_hit

        
    # create line equation
#day 10 2019
printf(g)
cors = {(a,b) for a in range(len(g)) for b in range(len(g[0]))}
# print(cors)

print(len(g), len(g[0]))
mv = -float('inf')
get_lines(cors, (19,11))
# print(topy, topx)
print("total len", mv)        
