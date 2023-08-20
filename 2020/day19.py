from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys
import copy

eg = False
inputLines = loadInput()
# inputLines = loadeg()
# eg = True
# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"
# opt 6: 7 | 8
#
# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb

        
    

m = dict()
i = 0
while i < len(inputLines):
    l = inputLines[i]
    if l == "":
        i += 1
        break
    else:
        if "|" in l:
            front,back = l.split("|")
            key,*p1 = front.split(" ")
            key = int(key[:-1])
            p1 = [int(x) for x in p1 if x.isnumeric()]
            p2 = [int(x) for x in back.split(" ") if x.isnumeric()]
        elif '\"' in l:
            pass
        else:
            key,*p1 = l.split(" ")  
            key = int(key[:-1])
            p1 = [int(x) for x in p1 if x.isnumeric()]
            p2 = []
        m[key] = (p1,p2)
    i += 1
    if not eg:
        m[35] = ("a",[])
        m[72] = ("b", [])
    else:
        m[4] = ("a",[])
        m[5] = ("b", [])


# generate also possible pairs, then check each one
# check each as going through
print(m)

def match_list(m ,rem, nums):
    for r_num in nums:
    # can't have run out of chars early
        if rem == "":
            return (False, "")
        is_match, rem = match(m, rem, r_num)
        if not is_match: # check if ran out of chars early
            return (False, "")  
    # print("match_list", rem, nums, "matches")
    return True, rem
# returns if those remainding chars match the current rule (without leaving any letters)
dp = {}
def match(m ,rem, rule):
    if rem == '':
        return True, ""
    # print(rule)
    # print(m, ",", rem)
    p1,p2 = m[rule]
    if type(p1) is str:
        if rem[0] == p1:
            return True, rem[1:]
        else:
            return False, ""
    orig_rem = copy.deepcopy(rem)
    (is_match, rem) = match_list(m, orig_rem, p1)
    if not is_match and len(p2) > 0:
        (is_match, rem) = match_list(m, orig_rem, p2)
    # print("is_match, rem", is_match, rem)
    
    if rule == 0 and rem != "":
        return False, ""
    return is_match, rem
    



t = 0
while i < len(inputLines):
    l = inputLines[i]
    did_match, result = match(m, l, 0)
    print(did_match, result)
    if did_match:
        t += 1
    i += 1
print(t)
# print(m)