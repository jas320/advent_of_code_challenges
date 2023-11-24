from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
inputLines = loadeg()

import os
print(os.getcwd())
print("SUCCESS")
print(inputLines)
quit()
inputLinesInt = [int(x) for x in inputLines]
inputLinesSet = set(inputLinesInt)
for x in inputLinesInt:
    diff = 2020 - x
    for y in inputLinesInt:
        diff2 = diff - y
        if diff2 in inputLinesSet:
            print(diff2, x, y, diff2 * x * y)


    