from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()
m1 = {"(":1, "[":2, "{":3, "<":4}
m2 = {")":"(","]":"[","}":"{",">":"<"}
print(inputLines)
t = 0
res = []
for l in inputLines:
    stack = []
    comp = True
    for c in l:
        if c in m2.keys():
            if len(stack) == 0 or stack[-1] != m2[c]:
                print("corrupted", c, "exp", stack[-1])
                # t += m1[m2[c]]
                comp = False
                break
            else:
                stack.pop()
        else:
            stack.append(c)
    if len(stack) > 0 and comp:
        #complete
        t = 0
        for c in reversed(stack):
            t *= 5
            t += m1[c]
        res.append(t)   
print(res)         
print(sorted(res)[len(res) // 2])    