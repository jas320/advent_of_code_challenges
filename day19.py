from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import os


inputLines = loadInput()
inputLines = loadeg()
for i in range(1, 10):
    os.rename(f"day{i}.py", f"day0{i}.py")