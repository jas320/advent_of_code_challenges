from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()

#944, 5 mins, bus 59
t = int(inputLines[0])
nums = [int(x) for x in inputLines[1].split(",") if x != 'x']
print(nums)
print([t // x for x in nums])
res = [((t // x) + 1) * x for x in nums]

min = min(res)
i = res.index(min)
print((min - t) * nums[i])
# print(min * nums[i])

    