from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()

c = 0
m2 = defaultdict(set)
m4 = {}
all = {'a','b','c','d','e','f','g'}
m3 = {k : set(all) for k in all} # letter mapping
print(m3)
lets = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcfd', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
nums = list(range(10))
input = {frozenset(a) : b for a, b in zip(lets,nums)}

def update(group, actual):
    for k in m3:
        if k not in group:
            m3[k] -= set(actual)
        else:
            m3[k] -= (all - set(actual))

t = 0
apperance = defaultdict(int)
for l in all:
    for group in lets:
        if l in group:
            apperance[l] += 1
print(apperance)
for i in range(len(inputLines)):
    m2.clear()
    for l in all:
        m3[l] = set(all)
    a, b = inputLines[i].split("|")
    prev = a.split(" ")[:-1]
    out = b.split(" ")[1:]
    i = 0
    for group in prev:
        for l in group:
            m2[l].add(group)
    for group in prev:
        if len(group) == 2:
            update(group, "cf")
        elif len(group) == 4:
            update(group, "bcfd")
        elif len(group) == 3:
            update(group, "acf")
        elif len(group) == 7:
            update(group, "abcdefg")
    for k in m3:
        v = m3[k]
        if v == set("cf"):
            is_in = m2[k]
            if len(is_in) == 9:
                update(k, "f")
        elif v == set("bd"):
            is_in = m2[k]
            # print("is_in", m2[k])
            if len(is_in) == 6:
                update(k, "b")
        elif v == set("ge"):
            is_in = m2[k]
            if len(is_in) == 4:
                update(k, "e")
    for k in m3:
        m3[k] = m3[k].pop()
    nums = ""
    for group in out:
        f = frozenset([m3[x] for x in group])
        nums += str(input[f])
    t += int(nums)
print(t)
    