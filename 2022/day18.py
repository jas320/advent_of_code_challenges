from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque,
import numpy as np


inputLines = loadInput()
# inputLines = loadeg()
s = set()
for x in inputLines:
    ls = x.split(",")
    a,b,c = ls
    s.add((int(a),int(b),int(c)))
ma, mb, mc = max(s, key=lambda a : a[0])[0], max(s, key=lambda a : a[1])[1], max(s, key=lambda a : a[2])[2]
mina,minb,minc = min(s, key=lambda a : a[0])[0], min(s, key=lambda a : a[1])[1], min(s, key=lambda a : a[2])[2]
eve = set()
for a in range(mina - 1, ma + 2):
    for b in range(minb - 1, mb + 2):
        for c in range(minc - 1, mc + 2):
            eve.add((a,b,c))

cv = set()
p = (mina - 1, minb - 1, minc - 1)
# p = (ma +1 ,mb + 1, mc + 1)
q = deque()
q.append(p)
cv = set()
from_to = set()
cv.add(p)
sides = 0
cube_m = {x : 0 for x in s}
print("start", p)
while len(q) > 0:
    curr = q.popleft()
    cv.add(curr)
    a,b,c = curr
    next = []
    for i in range(-1, 2, 2):
        next.append((a+i, b, c))
        next.append((a, b+i, c))
        next.append((a, b, c+i))
    for next_p in next:
        if next_p in s:
            # print("counting side", curr, next_p)
            sides += 1
            cube_m[next_p] += 1
        if next_p not in cv:
            cv.add(next_p)
            if next_p in s:
                pass
            elif next_p not in eve:
                # print("outside", next_p)
                pass
            else:
                # print("still going", next_p)
                q.append(next_p)
                       
# print(v)
for k,v in cube_m.items():
    print(k, v)
print(sides)
                    
 
                
                        