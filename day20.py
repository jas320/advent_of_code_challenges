from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import copy
import llist

def mangle(val, str):
    return f"{val}_{str}"

def valueof(str):
    if "_" in str:
        return int(str.split("_")[1])
    else:
        return int(str)

inputLines = loadInput()
# inputLines = loadeg()
p = {}
nl = inputLines
cnt = Counter(inputLines)
for i in range(len(inputLines)):
    s = inputLines[i]
    if s not in p:
        p[s] = 0
        nl[i] = mangle(p[s], s)
    else:
        p[s] += 1
        nl[i] = mangle(p[s], s)
print(nl)
# quit()
# nl = [int(x) for x in inputLines]
nl_d = copy.deepcopy(nl)
# on = {i : i for i in range(len(nl))}
# print(nl)
for i in range(len(nl_d)):
    n = nl_d[i]    
    # second = n.split("_")[1]
    vs = [n]
    # for x in range(cnt[second]):
    #     vs.append(f"{x}_{second}")
    # print(vs)
    for n in vs:
        # print(n)
        # second = (n.split("_"))[1]
        # n = "0_" + second
        start_i = nl.index(n)
        new_index = (start_i + valueof(n))
        if new_index == start_i:
            continue
        elif new_index > len(nl):
            new_index = (new_index) % len(nl)
        elif new_index <= 0:
            new_index = (new_index - 1) % len(nl)
        print(n, start_i, new_index)
        nl.insert(new_index + 1, n)
        # print(nl)\
        nl.pop(start_i if start_i < new_index else start_i + 1)
        # print(nl)
t = 0
for j in range(1000,3000 + 1,1000):
    start_i = nl.index("0_0")
    f = (start_i + j) % len(nl)
    # print(nl[f])
    t += valueof(nl[f])
print(t)
    
