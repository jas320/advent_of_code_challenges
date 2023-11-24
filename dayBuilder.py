# creates many python files
import os
toWrite = """from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
inputLines = loadeg()"""
year = 2021
root = os.path.dirname(__file__)
os.mkdir(root + "/" + str(year))
# print(os.getcwd())
for x in range(10,25):
    dayString = "0" + str(x) if x < 10 else str(x)
    print(dayString)
    f = open(root + "/" + str(year) + "/" + "day" + dayString + ".py", "w")
    f.write(toWrite)

    

    