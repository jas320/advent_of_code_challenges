from utils import loadInput


inputLines = loadInput()

h,w = len(inputLines), len(inputLines)[0]
g = [[-1] * w] * h
print(g)