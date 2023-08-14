from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys
import copy

inputLines = loadInput()
# inputLines = loadeg()
dc = copy.deepcopy(inputLines)
for i in range(0, len(inputLines)):
    old_val = inputLines[i]
    if old_val[:3] == "nop":
        dc[i] == "jmp" + old_val[3:]
    elif old_val[:3] == "jmp":
        dc[i] = "nop" + old_val[3:]
    else:
        continue
    acc = 0
    next_index = 0
    visited = set()
    inf = False
    while next_index < len(dc):
        if next_index in visited:
            inf = True
            break
        else:
            visited.add(next_index)
        l = dc[next_index]
        ins, amount = l.split(" ")
        sign, num = amount[0], amount[1:]
        if ins == "acc":
            acc = acc + (int(num) if sign == "+" else -1 * int(num))
        elif ins == "jmp":
            next_index = next_index + (int(num) if sign == "+" else -1 * int(num))
            continue
        next_index += 1
    if not inf:
        print(acc, i)
    
    dc[i] = old_val