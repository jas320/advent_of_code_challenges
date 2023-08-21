from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()
inputLines = [int(x) for x in inputLines]
wsize = 25
part1 = False

if part1:
    window = dict(Counter(inputLines[:wsize]))
    for i in range(wsize, len(inputLines)):
        n = inputLines[i]
        found = False
        for x in window.keys():
            if (n - x) in window and window[(n - x)] > 0:
                found = True
                break
        if not found:
            print(n)
            print(window)
            quit()
        # print(n, window)
        first = inputLines[i - wsize]
        window[first] -= 1 # value at earliest pos
        if window[first] == 0:
            window.pop(first)
        if n in window:
            window[n] += 1
        else:
            window[n] = 1

val = 2089807806
for ws in range(2, len(inputLines)):
    t = sum(inputLines[:ws])
    start = 0
    if t == val:
        ns = inputLines[start: start + ws]
        quit()
    while start + ws < len(inputLines):
        # print(start, start + ws)
        t -= inputLines[start]
        t += inputLines[start + ws]
        if t == val:
            ns = inputLines[start + 1: start + ws + 1]
            print(min(ns) + max(ns))
            quit()
        start += 1

    