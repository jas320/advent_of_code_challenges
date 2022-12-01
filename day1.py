import collections
import timeit
import sys
import os

def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()

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