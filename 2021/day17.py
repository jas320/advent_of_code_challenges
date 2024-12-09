from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
inputLines = loadeg()

#target area: x=169..206, y=-108..-68
x,y = (0,0)
# x1,x2,y1,y2 = 20,30,-10,-5


x1,x2,y1,y2 = 169,206,-108,-68
mv = -float('inf')
m1,m2 = 0, -300
res = (0,0)
overallmax = -float('inf')
seen = set()
for a in range(0, 1000):
    for b in range(-300, 1000):
        xvel, yvel = (a,b)
        x,y = (0,0)
        # print(f"{xvel=}{yvel=}")
        mv = -float('inf')
        inside = False
        while x < x2 and y > y1:
            x += xvel
            y += yvel
            xvel += (-1 if xvel > 0 else (0 if xvel == 0 else 1))
            yvel -= 1
            mv = max(y, mv)
            if x1 <= x <= x2 and y1 <= y <= y2: # inside target area
                inside = True
                seen.add(a,b)
        if inside: # any step landed inside
            seen.add((a,b))
            if mv > overallmax:
                res = (a, b)
                overallmax = mv
print("final", res, overallmax, len(seen))

    