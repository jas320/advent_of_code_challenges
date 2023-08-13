from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()

string = ""
i = 0
ls = []
lst = []
while i < len(inputLines):
    line = inputLines[i]
    if line == "":
        lst.append(ls)
        ls = []
    else:
        ls.append(line)
    i += 1
lst.append(ls)
lst = [" ".join(x) for x in lst]
# print(*lst, sep="\n")
# print(len(lst))
        
def digitBetween(value, length, start, end):
    if value.isdigit() and (len(value) == length) and (start <= int(value) <= end):
        return True
v = 0
for l in lst: 
    line = l.split(" ")
    fields = [f.split(":")[0] for f in line]
    kv = {f.split(":")[0] : f.split(":")[1] for f in line}
    if len(fields) == 8 or (len(fields) == 7 and ("cid" not in set(fields))):
        b1 = digitBetween(kv['byr'], 4, 1920, 2002)
        b2 = digitBetween(kv['iyr'], 4, 2010, 2020)
        b3 = digitBetween(kv['eyr'], 4, 2020, 2030)
        hs = kv['hgt']
        if (hs[-2:] == "in"):
            b4 = digitBetween(hs[:-2], 2, 59, 76)
        elif (hs[-2:] == "cm"):
            b4 = digitBetween(hs[:-2], 3, 150, 193)
        else:
            b4 = False
        str = kv['hcl']
        b5 = str[0] == '#' and str[1:].isalnum() and len(str[1:]) == 6
        if not b5:
            print(str)
        str = kv['ecl']
        b6 = str in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        str = kv['pid']
        b7 = str.isdigit() and len(str) == 9
        if b1 and b2 and b3 and b4 and b5 and b6 and b7:
            v += 1
        else:
            print("invalid", kv)
        # print(len(line))
        # print(line)
        # print(fields)

# 280 items
print(v)