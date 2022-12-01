import collections
import timeit
import sys
import os
from utils import loadInput


inputLines = loadInput()
b = []
o = []
for x in inputLines:
    if x != '':
        b.append(int(x))
    else:
        o.append(b)
        b = []
x = sorted(list(map(sum, o)), reverse=True)
print(x[0])     # part 1
print(sum(x[0 : 3]))    # part 2