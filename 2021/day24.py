from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()

def printf(x):
    print(f"{x = }")


ops = {"add": lambda a, b: a + b,
        "mul": lambda a, b: a * b,
        "div": lambda a, b: a // b,
        "mod": lambda a, b: a % b,
        "eql": lambda a, b: 1 if a == b else 0}

# start = 99999987654321
# start = 55555555555555
# start = 55555555555555
start = 12345678912845
# start = 111
# start = 99999999999999
inputLines = [x.split(" ") for x in inputLines]
for input in range(start, start - 1, -1):
    input_int = input
    m = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    input = list(str(input))
    MONAD = deque(input)
    for x in inputLines:
        op, a, *b = x
        if op == "inp":
            # m[a] = int(a)
            if len(MONAD) == 0:
                print(m, input_int)
                break
            m[a] = int(MONAD.popleft())
        else:
            b = b[0]
            if b in m:
                v2 = m[b] # get value
            else:
                v2 = int(b)
            v1 = int(m[a])
            
            res = ops[op](v1, v2)
            # print(op, a, "(", v1, ")", v2, "res=", res)
            m[a] = res
        print(m, x)
    # if m["z"] == 0:
    # print(input, m, bin(input_int))
    result = m["z"] == 0
    if result:
        print(input_int, "valid")
    print(m, input_int)
# print("got here")