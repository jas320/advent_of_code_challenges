from utils import loadInput, loadeg, grid
from collections import defaultdict, Counter, deque
import numpy as np
import copy


inputLines = loadInput()
inputLines = loadeg()
g = grid(inputLines)
w,h = len(g[0]), len(g)
start = (0, 1)
end = (len(g), len(g[0]) - 2)
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
            if len(v) == 1:
                s += v[0]
            else:
                s += str(len(v))
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

# pg(g)
# quit()
for t in range(5):
    print("count", t)
    pg(g)
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
                # print(char)
                x,y = new_d[char]
                i2,j2 = (i + x, j + y)
                i2,j2 = wrap(i2, j2)
                # print(g2[i2][j2])
                # print(char, (i,j), "moves to", (i2,j2))
                g2[i2][j2] = g2[i2][j2] + [char]
    for i in range(h):
        for j in range(w):
            if g2[i][j] == []:
                g2[i][j] = ["."]
    g = g2


