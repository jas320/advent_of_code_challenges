from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()

# parsing
all_ing, all_alle = set(), set()
ing_list = []
order = []
for l in inputLines:
    first, second = l.split(" (contains ")
    ings = set(first.split(" "))
    second = second.replace(")","")
    allegens = set(second.split(", "))
    order.append((ings, allegens))
    [ing_list.append(i) for i in ings]
    # print(ings, allegens)
    all_ing |= ings
    all_alle |= allegens
print(len(all_alle))
could_be = {x : set(all_ing) for x in all_alle}
for (ing,alle) in order:
    for a in alle:
        # print(a, "intersection of", could_be[a], ing, "is")
        could_be[a] &= ing
        # print(could_be[a])

# print(list(could_be.values()))
left = all_ing - set.union(*list(could_be.values()))
# print(left)
c = Counter(ing_list)
t = sum([c[i] for i in left])
print(t)
sortedKeyList = sorted(could_be.keys(), key=lambda s: len(could_be.get(s)))
res = {}
finished = False

while not finished:
    for key in sortedKeyList:
        if len(could_be[key]) == 1:
            item = could_be[key].pop()
            res[item] = key
            for v in could_be.values():
                v.discard(item)
    if len(res) == len(could_be):
        finished = True

alpha = [k for k, v in sorted(res.items(), key=lambda item: item[1])]
print(alpha)
#asner

# ltbj,nrfmm,pvhcsn,jxbnb,chpdjkf,jtqt,zzkq,jqnhd.
