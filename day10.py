from utils import loadInput
import numpy as np
w,h = 40,6

row = -1
pos = set([0,1,2])
crt = 0
g=  [["."]*w for _ in range(h)]


def add(num, cycle, x, val, r):
    global pos
    for c in range(num):
        check(cycle, x, r)
        cycle += 1
    x += val
    pos = set([x - 1, x , x + 1])
    return cycle, x

def check(cycle, x, r):
    global g
    global row
    if cycle > 220:
        return
    if ((cycle - 1) % 40) == 0:
        print(cycle, x)
        print(g)
        r.append(x * cycle)
        row += 1
    print("cycle: ", cycle, "row:", row, "sprite pos", pos, "x", x)
    g[row][((cycle - 1) % 40)] = "#" if (cycle - 1) % 40 in pos else "."

inputLines = loadInput()
cycle = 1
x = 1
r = []
ins = [("addx", int(l.split(" ")[1])) if len(l.split(" ")) > 1 else "noop" for l in inputLines]
for ins_ in ins:
    if ins_ == "noop":
        check(cycle, x, r)
        cycle += 1
    else:
        text, val = ins_
        cycle,x = add(2, cycle, x, val, r)
        
print(g)
[print(' '.join(g[i])) for i in range(len(g))]
print(np.sum(r))
                
        
        

    