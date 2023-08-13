from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import os
import copy

def canby(num, rob, costs, am):
    for i in range(num):
        for k,v in costs[rob]:
            if v > am[k]:
                return False
    return True
def canby_mul(i,j,k,l,rb,costs,am):
    pass   

def buy(rob, costs, am):
    for k,v in costs[rob]:
        am[k] -= v

def ways_buying(rb, costs, am):
    costs_d = copy.deepcopy(costs)
    am_d = copy.deepcopy(am)
    rb_d = copy.deepcopy(rb)
    max_each = {}
    for rob in rb:
        while canby(rob, costs_d, am_d):
            buy(rob)
        max_each[rob] = rb_d[rob] - rb[rob]
    for i in range(max_each["o"]):
        for j in range(max_each["c"]):
            for k in range(max_each["ob"]):
                for l in range(max_each["g"]):
                    pass
                    

inputLines = loadInput()
inputLines = loadeg()
t = ["o","c","ob","g"]
costs = {"o": {"o":4}, "c":{"o":2}, "ob":{"o":3, "c":14}, "g":{"o":2, "ob":7}}
am = {x : 0 for x in t}
rb = {x : 1 if x == "o" else 0 for x in t}
dp = {}
# dp maps current robots and amounts to max geodes (but we have varying n of rounds)
# all clay should be used for obisidian robot
# all obsidian robot should be used for geode

def max_num_geodes(rb, costs, am):
    c = 0
    while c < 24:
        for rob in t:
            if costs[rob]
        
        
        
        
        
        # update amount of each based on number of robots
        for k in t:
            am[k] += rb[k]