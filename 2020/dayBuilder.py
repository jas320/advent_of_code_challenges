# creates many python files
 
toWrite = """from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
inputLines = loadeg()"""
for x in range(1,25):
    dayString = "0" + str(x) if x < 10 else str(x)
    print(dayString)
    f = open("day" + dayString + ".py", "w")
    f.write(toWrite)

    

    