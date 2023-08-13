from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import copy
import llist

inputLines = loadInput()
# inputLines = loadeg()

nums = [int(x) for x in inputLines]
nums = [x * 811589153 for x in nums]
nums = deque(list(enumerate(nums)))
for t in range(10):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j][0] == i:
                break
        # print(nums[j])
        while nums[0][0] != i:
            nums.append(nums.popleft())
        val = nums.popleft()
        to_pop = val[1]
        to_pop %= len(nums)
        for _ in range(to_pop):
            nums.append(nums.popleft())
        nums.append(val)

for j in range(len(nums)):
    if nums[j][1] == 0:
        break

print(sum([nums[(j + i) % len(nums)][1] for i in range(1000,3001, 1000)]))
    
