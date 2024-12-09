from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()
# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2

m = defaultdict(int)
for l in inputLines:
    p1,p2 = l.split(" -> ")
    x1,y1 = p1.split(",")
    x2,y2 = p2.split(",")
    x1 = int(x1); x2 = int(x2); y1 = int(y1); y2 = int(y2)
    if y1 == y2:
        for x in range(x1, x2 + (1 if x2 >= x1 else -1), 1 if x2 >= x1 else -1):
            m[(y1, x)] += 1
    elif x1 == x2:
        for y in range(y1, y2 + (1 if y2 >= y1 else -1), 1 if y2 >= y1 else -1):
            m[(y, x1)] += 1
    else:
        l1 = list(range(y1, y2 + (1 if y2 >= y1 else -1), 1 if y2 >= y1 else -1))
        l2 = list(range(x1, x2 + (1 if x2 >= x1 else -1), 1 if x2 >= x1 else -1))
        for (y,x) in zip(l1, l2):
            m[(y, x)] += 1
        # print(list(zip(l1, l2)))
t = 0
# print(m)
for k, v in m.items():
    if v >= 2:
        t += 1
print("total", t)    

