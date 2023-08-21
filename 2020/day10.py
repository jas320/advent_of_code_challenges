from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import math
import sys

inputLines = loadInput()
inputLines = loadeg()
sn = sorted(list(map(int, inputLines)))
sn = [0] + sn
sn.append(sn[-1] + 3) # add highest voltage plus 3
sn_set = set(sn)
c,c2 = 0,0
prev = 0
part1 = False

if part1:
    print(sn)
    for x in sn:
        diff = x - prev
        if diff == 1:
            c += 1
        elif diff == 3:
            c2 += 1
        else:
            print("not 1 or three")
        prev = x
    print(c, c2)
    print(c * c2)

if not part1:
    # dp solution
    print(sn)
    dp = {}
    def arrange(start):
        if start == sn[-1]:
            res = 1
        elif start in dp:
            return dp[start]
        elif start not in sn_set:
            res = 0
        else:
            res = arrange(start + 1) + arrange(start + 2) + arrange(start + 3)
        dp[start] = res
        print(dp)
        return res
    print(arrange(sn[0]))
