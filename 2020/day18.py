from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2


def check_top(ns, str):
    if len(ns) > 0:
        top = ns.pop()
        ns.append(top)
        if top == str:
            return True
    return False

# two safe numbers of ns stack
def reduce_normal(ns, ops):
    op = ops.pop()
    n2,n1 = ns.pop(), ns.pop()
    r = n1 * n2 if op == "*" else n1 + n2
    ns.append(r)
# reduce down to next '(' called when hitting ")"
def reduce(ns, ops):
    hit_open = False
    nums = []
    while not hit_open:
        n = ns.pop()
        if n == "(":
            hit_open = True
        else:
            nums.append(n)
    if len(nums) == 2:
        n1,n2 = nums[0], nums[1]
        op = ops.pop()
        r = n1 * n2 if op == "*" else n1 + n2
        ns.append(r)
    elif len(nums) == 1:
        ns.append(nums[0])


def next_char_not_plus(line, idx):
    while idx < len(line):
        next_char = line[idx]
        if next_char != " ":
            if next_char != "+":
                return True
            else:
                return False
        idx += 1
    return True



ns = deque()
ops = deque()
t = 0
for m,l in enumerate(inputLines):
    # if m == 10:
    #     break
    for idx, c in enumerate(l):
        if c == "(":
            ns.append(c)
        elif c == ")":
            # eval stack up until ()
            reduce(ns, ops)
            while len(ns) >= 2 and type(ns[-1]) is int and type(ns[-2]) is int:
                if len(ops) > 0 and (next_char_not_plus(l, idx + 1) or (ops[-1] == "+")):
                    reduce_normal(ns, ops)
                else:
                    break
        elif c == "+":
            ops.append(c)
        elif c == "*":
            ops.append(c)
        elif c.isdigit():
            open_bracket = check_top(ns, "(")
            ns.append(int(c))
            while len(ns) >= 2 and type(ns[-1]) is int and type(ns[-2]) is int:
                if len(ops) > 0 and (next_char_not_plus(l, idx + 1) or (ops[-1] == "+")):
                    reduce_normal(ns, ops)
                else:
                    break
        else:
            continue
        # if m == 6:
        # print(ns, ops)
    while len(ns) > 1:
        reduce_normal(ns,ops)
    final = ns.pop()
    if (len(ops) != 0):
        print("bad", m)
        print(ops)
    print("total:", final)
    t += final
print("total", t)

# if hit * check next operator:
# if is * then collapse
# if its + then leave on stack