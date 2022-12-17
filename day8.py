from utils import loadInput
from collections import Counter
import heapq as hq
import copy
import numpy as np

inputLines = loadInput()

h,w = len(inputLines), len(inputLines[0])
g = [[-1]*w for _ in range(h)]
#brute force because cba
# compl wh * (w + h) = w^2h + h^2w
# invert mapping allowing us to use min heap implementation from "import heapq"
for i, line in enumerate(inputLines):
    for j, v in enumerate(line):
        g[i][j] = 9 - int(v)
# print(g)
def update(g, vis):
    # i is height in this case, j is width
    for i, line in enumerate(g):
        c_r = Counter(line)
        hp_r = list(set(line)) # about to be transformed into a heap, in place, linear time
        hq.heapify(hp_r)
        hp_l = []
        hq.heapify(hp_l)
        for j, v in enumerate(line):
            c_r[v] -= 1
            while hp_r:
                if c_r[hp_r[0]] == 0:
                    hq.heappop(hp_r)
                else:
                    break
            if not vis[(i,j)]:
                vis[(i, j)] = (v < (hp_l[0] if hp_l else 99)) or (v < (hp_r[0] if hp_r else 99))
            # print(g[i][j],hp_l, hp_r)
            hq.heappush(hp_l, v)

def slowUpdate(g, vis):
    for i, line in enumerate(g):
        l,r = [],line[1:]
        for j,v in enumerate(line):
            sc = 0
            for x in l[::-1]:
                sc += 1
                if x <= v:
                    break
            vis[(i,j)].append(sc)
            sc = 0
            for x in r:
                sc += 1
                if x <= v:
                    break
            vis[(i,j)].append(sc)
            # print(l,r,v,sc, vis[(i,j)])
            l.append(v)
            r = r[1:]
vis = {(i,j):[] for i in range(h) for j in range(w)}
# update(g, vis)
# print(vis)
# transpose to reuse cod efor other way
slowUpdate(g, vis)
trans_g = [list(i) for i in zip(*g)]
vis = {(i,j) : vis[(j,i)] for i in range(h) for j in range(w)}
# print("across")
# print(trans_g)
# update(trans_g, vis)
slowUpdate(trans_g, vis)
for i in range(h):
    for j in range(w):
        print(g[i][j], vis[(i,j)], " ", end="")
    print("\n")        
print(max([np.prod(vis[(i,j)]) for i in range(h) for j in range(w) if vis[(i,j)]]))
