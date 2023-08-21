from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import math
import sys
import re

inputLines = loadInput()
# inputLines = loadeg()

m = {}
part1 = False
if part1:
    for l in inputLines:
        lines = l.split(" ")
        if lines[0] == "mask":
            mask = lines[2] # string rep
        else:
            addr = re.split("mem\[", lines[0])
            addr = int(addr[1][:-1])
            num = int(lines[2])
            num_s = format(num, "#038b")[2:]
            mask_s = mask
            res = [mask_s[i] if mask_s[i] != "X" else num_s[i] for i in range(0, len(mask_s))]
            res = int("".join(res), 2)
            print(num)
            print(mask)
            print(res)
            print("\n")
            m[addr] = res
    quit()

# returns set of all binary combinations with the indexed bits on/off
def gen(indexes):
    r = {0}
    for i in indexes:
        temp = set()
        for xs in r:
            temp.add(2**i | xs)
        r = r.union(temp)
        # print(r)
    return r
# high = -1
for l in inputLines:
    lines = l.split(" ")
    if lines[0] == "mask":
        mask = lines[2] # string rep
    else:
        addr = re.split("mem\[", lines[0])
        addr = int(addr[1][:-1])
        num = int(lines[2])
        num_s = format(num, "#038b")[2:]
        addr_s = format(addr, "#038b")[2:]
        mask_s = mask
        base_num_s = [mask_s[i] if mask_s[i] == "1" else (addr_s[i] if mask_s[i] == "0" else "0") for i in range(0, len(mask_s))]
        indexes = []

        for i,v in enumerate(mask_s[::-1]):
            if v == "X":
                indexes.append(i)
        # print(addr)
        # print(addr_s)
        # print(mask_s)
        # print("".join(base_num_s))
        # print(indexes)
        base_num = int("".join(base_num_s), 2)
        combos = gen(indexes)
        addrs = [x + base_num for x in combos]
        # res = int("".join(res), 2)
        # print(addrs)??
        # quit()
        # print("\n")
        for a in addrs:
            m[a] = num
print(sum(m.values()))

