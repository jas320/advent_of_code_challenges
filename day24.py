from utils import loadInput, loadeg, grid
from collections import defaultdict, Counter, deque
import numpy as np
import copy
import sys
import math


inputLines = loadInput()
inputLines = loadeg()
g = grid(inputLines)
w,h = len(g[0]), len(g)

new_d = {"v" : (1,0), "^" : (-1,0), ">": (0,1), "<" : (0,-1)}
g = grid(inputLines)
for i in range(h):
    for j in range(w):
        g[i][j] = [g[i][j]]
def pg(g):
    for i in range(h):
        s = ""
        for j in range(w):
            v = g[i][j]
            s += v[0] if len(v) == 1 else str(len(v))
        print(s)
def wrap(i, j):
    if i == h - 1:
        i = 1
    elif i == 0:
        i = h - 2
    if j == 0:
        j = w - 2
    elif j == w - 1:
        j = 1
    return i,j

pos = [g]
# manual guessing : (, DFS not good with dp?
rounds = 1400
# we can abuse the fact that the position repeats every LCM modulo, times, this reduces the positions by a factor of the lcm.
rep = math.lcm(w - 2, h - 2)
for t in range(rep):
    g2 = [[[]]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            c = g[i][j]
            if c == ["."]:
                continue
            if c == ["#"]:
                g2[i][j] = c
                continue
            for char in c:
                x,y = new_d[char]
                i2,j2 = wrap(i + x, j + y)
                g2[i2][j2] = g2[i2][j2] + [char]
    for i in range(h):
        for j in range(w):
            if g2[i][j] == []:
                g2[i][j] = ["."]
    g = g2
    pos.append(g)
dp = {}
start = (0, 1)
def shortest(index, root, end):
    actual = (index % rep, root, end)
    # if we have reached this position before then just return that value
    if actual in dp:
        return dp[actual]
    if root == end:
        return index
    # optimisation to end once we hit a certain number of rounds (DFS not very reliable)
    if index + 1 >= rounds:
        return sys.maxsize - 1
    i,j = root
    out = []
    for x,y in [(1,0),(0,1),(0,0),(-1,0),(0,-1)]:
        i2,j2 = (i + x, j + y)
        if i2 < 0 or i2 > h - 1 or j2 < 0 or j2 > w - 1:
            continue
        if pos[(index + 1) % rep][i2][j2] == ["."]:
            out.append(shortest(index + 1, (i2,j2), end))
    dp[actual] = (min(out) if len(out) > 0 else sys.maxsize - 1)
    return dp[actual]
end2 = (h - 1, w - 2)
end2 = (h - 1,w - 2)

# this should be the length of the worst case path you are testing.
sys.setrecursionlimit(1500)
total = 0
s_e1 = shortest(0, start, end2)
print(s_e1)
