import os
from utils import loadInput

inp = loadInput()


def part1(inp):
    s = 0
    for i in range(0, len(inp), 3):
        a,b = inp[i], inp[i + 1]
        # b = inp[i + 1]
        c = inp[i + 2]
        res = (set(a).intersection(set(b))).intersection(set(c)) # should only contain 1 item
        res = list(res)[0]
        s2 = ord(res) - 96 if res.islower() else ord(res) - 38
        s += s2
        print(res ,s2)
    return s

def part1a(inp):
    s = 0
    n = 3
    for i in range(0, len(inp), n):
        prev = set(inp[i])
        for j in range(1, n):
            a = set(inp[i + j])
            prev = a.intersection(prev)
        res = list(prev)[0]
        s2 = ord(res) - 96 if res.islower() else ord(res) - 38
        s += s2
        print(res ,s2)
    return s    
    
# print(part1(inp)) 
print(part1a(inp)) 
    
    
    
    
    