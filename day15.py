from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import sys


inputLines = loadInput()
# inputLines = loadeg()


# cy = 2_000_000
# cy = 10
# outside = set()
lx = sys.maxsize - 1
hx = -sys.maxsize + 1
next = []
b = set()
check = set()
man = {}
for line in inputLines:
    l2 = line.replace("," ,"").replace("y", "").replace("x","").replace("=","").replace(":", "")
    sx,sy,bx,by = [int(x) for x in l2.split(" ") if x.isdigit() or x[0] == "-"]
    lx = min(lx, sx - abs(sx - bx))
    hx = max(hx, sx + abs(sx - bx))
    next.append((sx,sy,bx,by))
for (sx,sy,bx,by) in next:
    b.add((bx,by))
    manh = abs(sx - bx) + abs(sy - by)
    man[(sx,sy)] = manh
#     each_x = manh - dy
#     min_x,max_x = sx - each_x, sx + each_x
#     check = check.union({(cx, cy) for cx in range(min_x, max_x + 1)})
#     # print(sx,sy)
#     print(min_x, max_x)
# check = check.difference(b)

# bfs
for ((sx,sy), manh) in man.items():
    inc = [(1,1),(1,-1),(-1,-1),(-1,1)]
    x,y = (sx - manh - 1, sy)
    for inc_ in inc:
        for _ in range(manh + 1):
            if 0 <= x <= 4_000_000 and 0 <= y <= 4_000_000:
                r = True
                for ((sx2, sy2), manh2) in man.items():
                    if abs(x - sx2) + abs(y - sy2) <= manh2:
                        r = False
                        break
                if r:
                    print(x,y)
                    print(x * 4_000_000 + y)
                    quit()
                x,y = x + inc_[0], y + inc_[1]

        
    
# print(sorted(check))
# print(len(check))

    
    