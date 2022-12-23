from utils import loadInput
import math
import copy
def p():
    w,h = 40,40
    # for i,j in v:
    #     board[j][i] = "#"
    board = [["."]*w for _ in range(h)]
    board[h_[1]][h_[0]] = "H"
    for k in knotmap:
        a1, a2 = knotmap[k]
        board[a2][a1] = str(k)
    for i in range(h):
        for j in range(w):
            print(board[i][j], "", end="")
        print("\n")
    print("\n")

def move_t(t_, h_):
    a,b=t_;c,d=h_
    # print(t_,h_)
    # not adj
            
    if abs(a - c) > 1:
        if a < c:
            t_ = (c - 1, d)
        else:
            t_ = (c + 1, d)
    elif abs(d - b) > 1:
        if b < d:
            t_ = (c, d - 1)
        else:
            t_ = (c, d + 1)
    if (abs(a -c) + abs(d - b)) > 3:
        s = 999999
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                sc = (c + i, d + j)
                if (abs(c + i - a) + abs(d + j - b)) < s:
                    s = (abs(c + i - a) + abs(d + j - b)) 
                    s_v = sc
                    t_ = s_v
    # p(board, t_, v)   
    return t_

def move_k(knotmap, h_):
    for k in range(1, 10):
        if k == 1:
            k_ = move_t(knotmap[k], h_)
        else:
            # print(k, knotmap[k], knotmap[k-1])
            k_ = move_t(knotmap[k], knotmap[k - 1])
        knotmap[k] = k_
        knotset[k].add(k_)
        # p()
        

inputLines = loadInput()
global v
knotset = {x:set() for x in range(1,10)}
knotmap = {x:(10,30) for x in range(1,10)}
# board = [["."]*w for _ in range(h)]
h_ = (10, 30)
for l in inputLines:
    ins, n = l.split(" ")
    n = int(n)
    # print(ins, n)
    if ins == "R":
        for x in range(n):
            i,j = h_
            h_ = (i + 1, j)
            move_k(knotmap, h_)
    elif ins == "L":
        for x in range(n):
            i,j = h_
            # print(i,j)
            h_ = (i - 1, j)
            move_k(knotmap, h_)
    elif ins == "U":
        for x in range(n):
            i,j = h_
            h_ = (i, j - 1)
            move_k(knotmap, h_)

    elif ins == "D":
        for x in range(n):
            i,j = h_
            h_ = (i, j + 1)
            move_k(knotmap, h_)
    # p()
knotset[9].add((10,30))
# print(v)
for k in knotset:
    print(len(knotset[k]))
# print(len(knotset[9]))
# p()