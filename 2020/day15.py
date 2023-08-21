from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import math
import sys
import copy

inputLines = loadInput()
# inputLines = loadeg()

ranges = []
your_tick, near_tick = [],[]
it = iter(inputLines)
while True:
    l = next(it)
    if l == "":
        next(it)
        tickets = next(it)
        # print(tickets)
        your_tick.append(list(map(int, tickets.split(","))))
        break
    split = l.split(" or ")
    # print(split)
    a,b = split[0].split(" ")[-1].split("-")
    c,d = split[1].split("-")
    ranges.append(tuple(map(int, [a,b,c,d])))
    # print(a,b,c,d)
next(it)
next(it)
# print(your_tick)
while True:
    try:
        l = next(it)
        near_tick.append(list(map(int, l.split(","))))
    except StopIteration:
        break
# print(near_tick)


v = set()
m = {}
m2 = {}
m3 = {i : set() for i in range(len(ranges))}
for idx,(a,b,c,d) in enumerate(ranges):
    r1 = set(range(a,b+1))
    r2 = set(range(c,d+1))
    r3 = r1.union(r2)
    m2[idx] = r3
    v = v.union(v, r1.union(r2))
t = 0
# m indexes
m4 = {}
# print(len(near_tick))
near_tick_2 = []
for ls in near_tick:
    res = True
    for y in ls:
        if y not in v:
            res = False
            # print(y)
    if res:
        near_tick_2.append(ls)
# print(len(near_tick))
near_tick = near_tick_2
near_tick.append(your_tick[0])
for x in range(len(near_tick[0])):
    col = set()
    for y in range(len(near_tick)):
        col.add(near_tick[y][x])
        # print(f"{near_tick[y][x]},", end="")
    # print(col)
    m4[x] = col
    for z in range(len(ranges)):
        if col.issubset(m2[z]):
            m3[z].add(x)
# print(m4)
# print(m2)
# print(m3)
# print(your_tick)
# a: 1,5,6,8
# b: 3,7,9,10
# c: 1,4,5
# d: 5,6,7
# e: 1,4,5
# map of cat index to col indexes

1,2,3,4,5,6
print(m3)
sorted_values = sorted(m3.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in m3.keys():
        if m3[k] == i:
            sorted_dict[k] = m3[k]

dp = {} # not even used -_-
def fix_remaining(rm, rem_map, rem_cat):
    key = (frozenset(rem_cat), frozenset(rm.values()))
    if key in dp:
        print("hi")
        return dp[key]
    # if no cats left then everything has been fixed so return rm
    # fix a new cat with a new point
    # recurse passing refernece to rm with extra point fixed and popping from remaining
    if len(rem_cat) == 0:
        # valid solution
        dp[key] = (True, rm)
        return dp[key]

    for new_cat in sorted_dict:
        temp2 = copy.deepcopy(rem_cat)
        if new_cat in rem_cat:
            temp2.remove(new_cat)
            for new_col in rem_map[new_cat]:
                temp = copy.deepcopy(rem_map)
                [value.remove(new_col) for value in temp.values() if new_col in value]
                rm[new_cat] = new_col
                res, output = fix_remaining(rm, temp, temp2)
                dp[key] = (res, output)
                if (res == True):
                    return (res, output)
                rm[new_cat] = -1
    dp[key] = (False,{})
    return dp[key]

rm = {}
rem_cat = set(range(len(ranges)))
rem_map = copy.deepcopy(m3)
print(fix_remaining(rm, rem_map, rem_cat))

t = 1
for cat_i,col_i in rm.items():
    range_vals = m2[cat_i]
    col_vals = m4[col_i]
    if cat_i < 6:
        t *= your_tick[0][col_i]
    print(cat_i, col_i, col_vals.issubset(range_vals))
print(t)