from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys
import copy

inputLines = loadInput()
inputLines = loadeg()


# mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)

# brute force approach
# loop through allerges, assign ingredients see if it works
# add some optimisation

some_map = defaultdict(set)
assign = {}
for l in inputLines:
    ing, alle = l.split("(")
    ing_names = ing.split(" ")[:-1]
    alle_names = alle[9:-1]
    alle_names = alle_names.split(", ")
    print(ing_names, alle_names)
    for name in alle_names:
        some_map[name] = some_map[name].union(ing_names)
print(some_map)

all_ings = set.union(*some_map.values())
ings_never_used = all_ings

def solve(m, left_to_fix, current_mapping):
    global ings_never_used
    if len(left_to_fix) == 0:
        # print(m.values())
        ings_left = all_ings.difference(current_mapping.values())
        ings_never_used = ings_never_used.intersection(ings_left)
        # print("ended", current_mapping)
        print(len(current_mapping))
        # print("ings_left", ings_left)
        # unused_ings = unused_ings.intersection(ings_left)
        return
    
    next_alleg = left_to_fix.pop()
    next_ing_set = m[next_alleg]
    if len(next_ing_set) == 0:
        left_to_fix.add(next_alleg)
        return
    
    m_temp = copy.deepcopy(m)
    current_mapping_temp = copy.deepcopy(current_mapping)
    next_ing_set_fixed = copy.deepcopy(next_ing_set)
    left_to_fix_temp = copy.deepcopy(left_to_fix)
    for next_ing in next_ing_set_fixed:
        # print("fixing", next_alleg, "setting", next_ing)
        # print(left_to_fix)
        for vs in m_temp.values():
            if next_ing in vs:
                vs.remove(next_ing)
        # rem_fix = left_to_fix_temp.remove(next_ing)
        # print("2")
        current_mapping_temp[next_alleg] = next_ing
        print("current_mapping", current_mapping)
        solve(m_temp, left_to_fix_temp, current_mapping_temp)
        # backtrack in dfs
        # print("3")
        m_temp = m
        current_mapping_temp = current_mapping
        left_to_fix_temp = left_to_fix
    return
    

# print(unused_ings)
solve(some_map, set(some_map.keys()), dict())
print(ings_never_used)