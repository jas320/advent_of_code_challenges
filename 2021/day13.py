from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys
import copy

inputLines = loadInput()
# inputLines = loadeg()
m = {}
base = inputLines[0]
for l in inputLines[2:]:
    k,v = l.replace(" ","").split("->")
    m[k] = v
print(m)
step = 40
m2 = defaultdict(int)
freq = defaultdict(int)
for i in range(len(base) - 1):
    pair = base[i : i + 2]
    m2[pair] += 1
c = Counter(base)
    
# print(m2)
occur = {}
for counter in range(step):
    # key_set = frozenset(m2.keys())
    # m2.clear()
    m3 = defaultdict(int)
    occur = defaultdict(int)
    print(m2, counter)
    prev = None
    for k,v in m2.items():
            
        k1 = k[0] + m[k]
        k2 = m[k] + k[1]
        m3[k1] += v
        m3[k2] += v
        c[m[k]] += v # increase frequency of new letters
    # print(base)
    # print(len(base))
    m2 = m3

sorted = c.most_common(len(c.keys()))
print(sorted)
print(sorted[0][1] - sorted[-1][1])



