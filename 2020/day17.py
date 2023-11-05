from utils import loadInput, loadeg, grid
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()
part1 = False
# both parts identical just part 2 has 4-dimensions so code takes longer.
if part1:
    cubes = dict()
    s = grid(inputLines)
    print(s)
    for a in range(len(s[0])):
        for b in range(len(s)):
            if s[a][b] == "#":
                cubes[(a,b,0)] = 1 # active
            else:
                cubes[(a,b,0)] = 0
    for i in range(6):
        prev_keys = frozenset(cubes.keys())
        for (x,y,z) in prev_keys:
            for a in (-1,0,1):
                for b in (-1,0,1):
                    for c in (-1,0,1):
                        new = (x+a,y+b,z+c)
                        if new not in cubes:
                            cubes[new] = 0

        keys = frozenset(cubes.keys())
        swap = set()
        # alternatively make deepcopy and do changes on that (similar O(n))
        for key in keys:
            x,y,z = key
            active_n = set()
            for a in (-1,0,1):
                for b in (-1,0,1):
                    for c in (-1,0,1):
                        new = (x+a,y+b,z+c)
                        if new in cubes and cubes[new] == 1:
                            active_n.add(new)
            active_n.discard(key)
            
            if cubes[key] == 1:
                if len(active_n) == 2 or len(active_n) == 3:
                    pass
                else:
                    swap.add(key)
            else:
                if len(active_n) == 3:
                    swap.add(key)
        for key in swap:
            cubes[key] = 1 if cubes[key] == 0 else 0

        t = 0
        for k,v in cubes.items():
            if v == 1:
                t += 1
        print(t)
else:
    cubes = dict()
    s = grid(inputLines)
    print(s)
    for a in range(len(s[0])):
        for b in range(len(s)):
            if s[a][b] == "#":
                cubes[(a,b,0,0)] = 1 # active
            else:
                cubes[(a,b,0,0)] = 0
    for i in range(6):
        prev_keys = frozenset(cubes.keys())
        for (x,y,z,w) in prev_keys:
            for a in (-1,0,1):
                for b in (-1,0,1):
                    for c in (-1,0,1):
                        for d in (-1,0,1):
                            new = (x+a,y+b,z+c,w+d)
                            if new not in cubes:
                                cubes[new] = 0

        keys = frozenset(cubes.keys())
        swap = set()
        # alternatively make deepcopy and do changes on that (similar O(n))
        for key in keys:
            x,y,z,w = key
            active_n = set()
            for a in (-1,0,1):
                for b in (-1,0,1):
                    for c in (-1,0,1):
                        for d in (-1,0,1):
                            new = (x+a,y+b,z+c,w+d)
                            if new in cubes and cubes[new] == 1:
                                active_n.add(new)
            active_n.discard(key)
            
            if cubes[key] == 1:
                if len(active_n) == 2 or len(active_n) == 3:
                    pass
                else:
                    swap.add(key)
            else:
                if len(active_n) == 3:
                    swap.add(key)
        for key in swap:
            cubes[key] = 1 if cubes[key] == 0 else 0

        t = 0
        for k,v in cubes.items():
            if v == 1:
                t += 1
        print(t)