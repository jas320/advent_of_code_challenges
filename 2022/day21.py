from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
""" helper functions"""
def rec5(exp):
    next = m_[exp]
    if len(next) == 1:
        return next[0]
    else:
        first,op,second = next
        return "(" + rec5(first) + ")" + op + "(" + rec5(second) + ")"
def rec(exp, v):
    next = m_[exp]
    if next[0] == "x":
        return v
    else:
        first,op,second = next
        left = rec5(first)
        right = rec5(second)
        if "x" in left:
            v = eval(str(v) + new_op(op) + str(eval(right)))
            return rec(first, v)
        else:
            if op == "/":
                v = eval(str(eval(left)) + "*" + str(v))
            elif op == "-":
                v = eval(str(eval(left)) + "-" + str(v))
            else:
            # x in right
                v = eval(str(v) + new_op(op) + str(eval(left)))
            return rec(second, v)
def new_op(op):
    if op == "+":
        return "-"
    elif op == "-":
        return "+"
    elif op == "/":
        return "*"
    elif op == "*":
        return "/"

inputLines = loadInput()
# inputLines = loadeg()
""" pre processing """
m_ = {}
for x in inputLines:
    x = x.replace(":", " =")
    res = x.split(" ")
    # print(res)
    if res[2].isdigit():
        var,assign, first = res
        m_[var]= (first,)
    else:
        var,assign,first,op,second = res
        m_[var] = (first, op, second)
        
""" part 2"""
m_["humn"] = ("x",)
first, op, second = m_["root"]
left,right = rec5(first), rec5(second)
if "x" in left:
    v = eval(right)
    print(rec(first, v))
else:
    v = eval(left)
    print(rec(second, v))