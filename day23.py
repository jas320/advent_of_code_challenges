from utils import loadInput, loadeg, grid, xy_cors
from collections import defaultdict, Counter, deque
import numpy as np

def printM(loc):
    y1,y2,x1,x2 = xy_cors(list(loc.keys()))
    g = [["#" if (i,j) in loc else "." for j in range(x1, x2 + 1)] for i in range(y1, y2 + 1)]
    for l in g:
        print("".join(l))
    print("-- \n")
def no_other(loc, i, j):
    for k in [-1,0,1]:
        for m in [-1,0,1]:
            if k == 0 and m == 0:
                continue
            if (i +k, j +m ) in loc:
                return False
    return True
inputLines = loadInput()
# inputLines = loadeg()
g = grid(inputLines)
loc = {}
for i in range(len(g)):
    for j in range(len(g[0])):
        if g[i][j] == "#":
            loc[(i,j)] = g[i][j]
print(len(loc))
q = deque(["n", "s", "w", "e"])
pos_q = {x : [] for x in q}
t_p = {"n" : (-1, 0), "s" : (1, 0), "e" : (0, 1), "w": (0, -1)}
m = True
c = 0
while m:
    map2 = {}
    c += 1
    # print(q)
    # print("Round", r)
    m = False
    for i,j in loc.keys():
        if no_other(loc, i, j):
            continue
        m = True
        for dir in q:
            if dir == "n":
                if (i - 1, j -1) not in loc and (i - 1, j) not in loc and (i - 1, j + 1) not in loc:
                    map2[(i,j)] = (i - 1,j)
                    break
            if dir == "s":
                if (i + 1, j -1) not in loc and (i + 1, j) not in loc and (i + 1, j + 1) not in loc:
                    map2[(i,j)] = (i + 1,j)
                    break
            if dir == "w":
                if (i - 1, j - 1) not in loc and (i, j - 1) not in loc and (i + 1, j - 1) not in loc:
                    map2[(i,j)] = (i,j - 1)
                    break
            if dir == "e":
                if (i - 1, j  + 1) not in loc and (i, j + 1) not in loc and (i + 1, j + 1) not in loc:
                    map2[(i,j)] = (i,j + 1)
                    break
    # print(map2)
    count = Counter(list(map2.values()))
    for k,v in map2.items():
        if count[v] == 1:
            loc[v] = "#"
            loc.pop(k)
    q.append(q.popleft())
    keys = list(loc.keys())
    y1,y2,x1,x2 = min(keys, key=lambda x : x[0])[0], max(keys, key=lambda x : x[0])[0], min(keys, key=lambda x : x[1])[1], max(keys, key=lambda x : x[1])[1]
    # printM(loc)

keys = list(loc.keys())
y1,y2,x1,x2 = min(keys, key=lambda x : x[0])[0], max(keys, key=lambda x : x[0])[0], min(keys, key=lambda x : x[1])[1], max(keys, key=lambda x : x[1])[1]  
total = ((x2 - x1) + 1) * ((y2 - y1) + 1)
print(y1,y2,x1,x2)
print("total", total)
print("final", total - len(loc))
print(c)
