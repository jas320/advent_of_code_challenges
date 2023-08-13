from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
inputLines = loadeg()

cv = {"-": -1, "=": -2}
s = 0
c = 20
for l in inputLines:
    t = 0
    m = 1
    for c in reversed(l):
        if c in cv:
            v = cv[c]
        else:
            v = int(c)
        t += m * v
        m *= 5
    print(l, t)
    s += t
diff = s
cf = [5 ** i for i in range(20,-1,-1)]
cf2 = [2 * 5 ** i for i in range(20, -1, -1)]
t = 0
for j in range(len(cf2) -1, -1, -1):
    t += cf2[j]
    cf2[j] = t
cf.append(0)
cf2.append(0)

for i in range(20):
    if diff > cf[i]:
        break
i -= 1
res = []
neg = False
while i < len(cf2) - 1:
    print(abs(diff), cf[i], cf2[i+1])
    f = False
    for q in range (0, 3):
        if f:
            continue
        q = -q if neg else q
        if abs(diff - q * cf[i]) <= cf2[i + 1]:
            diff = diff - q * cf[i]
            if diff < 0:
                neg = True
            else:
                neg = False
            res.append(q)
            # print(q, diff)
            i += 1
            f = True

res = [x if x >= 0 else ("-" if x == -1 else "=") for x in res]
print(res)
print("".join(list(map(str,res))).lstrip('0'))
# for i in range(len(cf)):
    
    

        