from utils import loadInput
import os
from collections import Counter


inputLines = loadInput()
# sliding window
for l in inputLines:
    map_ = Counter(l[0:14])
    for i in range(14, len(l) - 3):
        c = l[i]
        if c in map_:
            map_[c] += 1
        else:
            map_[c] = 1
        d = l[i - 14]
        map_[d] -= 1
        if map_[d] == 0:
            map_.pop(d, None)
        if len(map_) == 14:
            print(i + 1)
            exit()
    
            
        