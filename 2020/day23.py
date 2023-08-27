from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()

cups = deque([int(x) for x in inputLines[0]])
final_n = 20
for i in range(10, final_n):
    cups.append(i)
max_n = max(cups)
cups.rotate(-1)
# quit()
print(cups)

# last cup on the right is current cup
dp = {}
for x in range(1_000_000):
    key = (tuple(cups))
    if key in dp:
        print("move", x + 1, "curr", curr)
        print("dp")
        print(cups)
        # break
    else:
        dp[key] = 1
    curr = cups[-1]
    a,b,c = cups.popleft(),cups.popleft(),cups.popleft()
    # print(cups, [a,b,c])
    dest = cups[-1] - 1
    picked = {a,b,c}
    if dest < 1:
            dest = max_n
    while dest in picked:
        dest -= 1
        if dest < 1:
            dest = max_n
    # print(dest, cups)
    while cups[-1] != dest:
        # print(dest, cups)
        cups.rotate(1)
    # print(cups)
    cups.appendleft(c)
    cups.appendleft(b)
    cups.appendleft(a)
    # print(cups)
    while cups[-2] != curr:
        cups.rotate(1)
    # sets up old curr to cups[-2] and new curr cups[-1]
    # print(cups)    
while cups[0] != 1:
    cups.rotate(1)
# print("".join(map(str,cups)))

    