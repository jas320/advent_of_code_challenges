from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()
v = 0
for l in inputLines:
    
    nums,letter,passw = l.split(" ")
    n1, n2 = nums.split("-")
    letter = letter[0]
    # c = Counter(passw).get(letter)
    # if c is None:
        # continue
    n1,n2 = int(n1), int(n2)
    if bool(passw[n1 - 1] == letter) ^ bool(passw[n2 - 1] == letter):
        print("valid", passw)
        v += 1
    # # if c >= int(n1) and c <= int(n2):
    #     print("valid", passw)
    #     v += 1
print(v)
    