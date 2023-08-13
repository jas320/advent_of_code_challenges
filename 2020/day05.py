from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()
# BFFFBBFRRR
# FFFBBBFRRR
# BBFFBBFRLL
ids = []
for l in inputLines:
    row,col,start,end,startc,endc = 0,0,0,128,0,8
    for c in l:
        if c == "F":
            end = (start + end) // 2
        if c == "B":
            start = (start + end) // 2
        if c == "L":
            endc = (startc + endc) // 2
        if c == "R":
            startc = (startc + endc) // 2
    # print("row:", start ,"col", startc, "id", start * 8 + startc)
    ids.append(start * 8 + startc)
maxrow = 128 * 8 + 7

print(max(ids))
ids.sort()
prev = ids[0]
print(ids)
for x in ids[1:]:
    if x - prev == 2:
        print(x, prev)
    prev = x
