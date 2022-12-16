from utils import loadInput
import re

inputLines = loadInput()

# can use either list for amortized (O(1)) from the back or use
# dequeue import
s = 0
for i in range(0, len(inputLines)):
    if inputLines[i][1] == '1':
        s = i
        e = int(inputLines[i][-2])
        print(s, e)
        break
g = []
for j in range(e):
    b = []
    for k in range(s - 1, -1, -1):
        c = inputLines[k][4 * (j+1) - 3]
        if c != " ":
            b.append(c)
    g.append(b)
print(g)
for i in range(s + 2, len(inputLines)):
    a = inputLines[i].split(" ")
    num,start,end = [int(d) - 1 for d in a if d.isdigit()]
    if num > 1:
        g[end] += g[start][-num:]
        g[start] = g[start][:-num]
        continue
    for j in range(num):
        g[end].append(g[start].pop())
print(g)
for x in g:
    print(x[-1], end="")