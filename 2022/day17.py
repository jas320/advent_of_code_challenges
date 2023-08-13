from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
from operator import itemgetter
import numpy as np


inputLines = loadInput()
# inputLines = loadeg()
w = 7
highest = (0,-1) # indicates highest rock, y-value, for spawning and hitting
def rock(type, s):
    x,y = s
    if type == "a":
        return {(x + i ,y) for i in range(4)}
    elif type == "b":
        return {(x + i, y + j) for i,j in [(0,1),(1,0),(1,1),(1,2),(2,1)]}
    elif type == "c":
        return {(x + i, y + j) for i, j in [(0,0),(1,0),(2,2),(2,1),(2,0)]}
    elif type == "d":
        return {(x, y + j) for j in range(4)}
    else:
        return {(x + i, y + j) for i in range(2) for j in range(2)}
    
def shift(right, set_, grid):
    new_s = set()
    for x,y in set_:
        if right:
            if x == w - 1 or (x+1,y) in grid:
                return set_
            new_s.add((x + 1, y))
        else:
            if x == 0 or (x-1,y) in grid:
                return set_
            new_s.add((x - 1, y))
    return new_s

types = ["a","b","c","d","e"]
grid = {(x,-1) for x in range(7)}
c = 0
moves = inputLines[0]
i = 0
dp = {}
while True:
    for x in types:
        start = (2, highest[1] + 4)
        new = rock(x, start)
        while True:
            if i == len(moves):
                i = 0
            move = moves[i]
            # print(move)
            # for j in range(start[1], -1, -1):
                # print("".join(["#" if (i,j) in grid or (i,j) in new else "." for i in range(7)]))
            new = shift(move == ">", new, grid)
            i += 1
            # print(new)
            # print(highest[1])
 
            # print("--------------")
            new2 = {(x, y - 1) for x,y in new}
            if not grid.isdisjoint(new2):
                break
            # print(new)
            # print(grid)
            new = new2
        for x in new:
            grid.add(x)
        rem = set()
        for y in range(min(new, key=itemgetter(1))[1] - 1, max(new, key=itemgetter(1))[1] + 2):
            pos_ = [(x,y) for x in range(7) if (x,y) not in grid]
            if len(pos_) == 0:
                for x2, y2 in grid:
                    if y2 < y:
                        rem.add((x2,y2))
            if len(pos_) == 1:
                x2,y2 = pos_[0]
                if (x2,y2 + 1) in grid or (x2, y2 + 2) in grid:
                    for x2, y2 in grid:
                        if y2 < y:
                            rem.add((x2,y2))
            if len(pos_) == 2:
                x2,y2 = pos_[0]
                x3,y3 = pos_[1]
                if (x2,y2 + 1) in grid and (x3, y3 + 1) in grid:
                    for x2, y2 in grid:
                        if y2 < y:
                            rem.add((x2,y2))
        grid = grid - rem
                
                
        # print(c, grid)
        highest = max(grid, key = lambda x : x[1])
        if c == 100000:
            print(len(grid))
            print(c,highest)
            # for j in range(start[1], -1, -1):
                # print("".join(["#" if (i,j) in grid or (i,j) in new else "." for i in range(7)]))
            quit()
        c += 1
        # print("next c")
print(highest)
                
                
                
        