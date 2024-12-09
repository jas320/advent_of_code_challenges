from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()

lines = [int(x) for x in inputLines[0].split(",")]
def dist(x):
    return (x * (x +1)) / 2
print(len(lines))
mv = float('inf')
for i in range(min(lines), max(lines) + 1):
    t = 0
    for j in range(len(lines)):
        diff = dist(abs(lines[j] - i))
        t += diff
    mv = min(mv, t)
print("minimum total", mv)
    
        