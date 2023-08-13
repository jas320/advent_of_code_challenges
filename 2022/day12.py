from utils import loadInput, grid
from collections import deque


inputLines = loadInput()

h,w = len(inputLines), len(inputLines[0])
g = grid(inputLines)
for i in range(h):
    for j in range(w):
        if g[i][j] == "S":
            g[i][j] = chr(ord("b") - 1)
        if g[i][j] == "E": g[i][j] = chr(ord("z") + 1)
starts = []
for i in range(h):
    for j in range(w):
        if g[i][j] == "a":
            starts.append(((i,j)))
ps = []
for start in starts:
    v = set()
    q = deque()
    q.append(start)
    v.add(start)
    bfs = []
    # print(g)
    pred = {}
    reach = False
    while len(q) > 0:
        curr = q.popleft()
        bfs.append(curr)
        i,j = curr
        if g[i][j] == chr(ord("z") + 1):
            reach = True
            break
        next = []
        if j != w - 1:
            next.append((i, j + 1))
        if j != 0:
            next.append((i, j - 1))
        if i != 0:
            next.append((i - 1, j))
        if i != h - 1:
            next.append((i + 1, j))
        # print([g[i][j] for i,j in next], g[i][j])
        next = [(k,m) for k,m in next if ord(g[k][m]) <= ord(g[i][j]) + 1]    
        for p in next:
            if p not in v:
                v.add(p)
                q.append(p)
                pred[p] = curr
    path = []
    while (i,j) != start:
        # print(g[i][j])
        i,j = pred[(i,j)]
        path.append((i,j))
    path = path[::-1]
    if reach:
        ps.append(len(path))
print(min(ps))