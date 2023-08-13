from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()

d = {}
# for l in inputLines:
#     words = l.split(" ")
#     if words[4] == "no":
#         continue
#         # d[words[1] + words[2]] = []
#     else:
#         res = []
#         for i in range(5, len(words) - 1, 4):
#             res.append(words[i] + words[i + 1])
#         value = words[0] + words[1]
#         for key in res:
#             if key in d:
#                 d[key].add(value)
#             else:
#                 d[key] = {value}
# print(d)
# # exit(0)
# queue = deque(["shinygold"])
# c = 0
# dyn = {}
# visited = set("shinygold")
# # breath first search
# while (len(queue) != 0):
#     curr = queue.popleft()
#     # print(curr)
#     if curr != "shinygold":
#         c += 1
#     next_items = d[curr] if curr in d else []
#     # print(next_items)
#     for x in next_items:
#         if x not in visited:
#             queue.append(x)
#             visited.add(x)
# print(c)

# depth first search
for l in inputLines:
    words = l.split(" ")
    if words[4] == "no":
        d[words[0] + words[1]] = []
    else:
        res = []
        for i in range(5, len(words) - 1, 4):
            res.append((int(words[i - 1]), words[i] + words[i + 1]))
        key = words[0] + words[1]
        for pair in res:
            if key in d:
                d[key].add(pair)
            else:
                d[key] = {pair} # pair = (1, lightblue), (number, name)
c = 0
links = d
dp = {}
print(d)
# exit(0)
print(links)

# recursive depth first search, memoisation (dynamic programming, both dicts referened as global variables)
def num_bags(bagname):
    # print(dp)
    if bagname in dp:
        return dp[bagname]
    else:
        dp[bagname] = sum([num + num * num_bags(name) for (num, name) in links[bagname]]) 
        return dp[bagname]
print(num_bags("shinygold"))
