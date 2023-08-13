from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()
inputLines.append("")
# print(inputLines)

curr = []
t = 0
for l in inputLines:
    if l == "":
        # print(curr)
        result_set = set(curr[0])
        for letters in curr[1:]:
            result_set = result_set.intersection(set(letters))
        # curr = "".join(curr)
        # print(result_set)
        t += len(result_set)
        curr = []
    else:
        curr.append(l)
print(t)
