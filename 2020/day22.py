from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()

# parse list into stack (deque of ints for each player)
# while both stacks have >1 item
# 	pop from each stack and compare
# 	add to bottom of winner stack (appendLeft, with winer card first)
# calc score by iterating over.
a,b,c,d = 1,26,28,53
# a,b,c,d = 1,6,8,13
p1 = deque([int(inputLines[i]) for i in range(a, b)])
p2 = deque([int(inputLines[i]) for i in range(c, d)])
print(p1,p2)
# quit()
def recursive_combat(p1, p2, dp):
    while p1 and p2:
        key = (tuple(p1),tuple(p2))
        # print("round: ", r, p1,p2)
        if key in dp:
            # p2 = []
            # print("inside")
            return p1,p2
        else:
            # print("got here")
            dp[key] = 1
        t1,t2 = p1.popleft(), p2.popleft()

        if len(p1) >= t1 and len(p2) >= t2:
            # recursive combat
            # print("recurse")
            p1_n = deque(list(p1)[:t1])
            p2_n = deque(list(p2)[:t2])
            p1_w,p2_w = recursive_combat(p1_n, p2_n, dict())
            p1_wins = len(p1_w) > 0
            p2_wins = len(p2_w) > 0
        else:
            p1_wins = t1 > t2
            p2_wins = t1 < t2

        if p1_wins:
            p1.append(t1)
            p1.append(t2)
        elif p2_wins:
            p2.append(t2)
            p2.append(t1)
        else:
            p1.append(t1)
            p2.append(t2)
        # print(f"{p1_wins} p1_wins")
        # print("after",p1,p2)
    return p1,p2
t = 0
p1,p2 = recursive_combat(p1,p2, dict())
# print(dp)
print(p1,p2)
winner = p1 if p1 else p2
for idx,v in enumerate(winner):
    t += (len(winner) - idx) * v
    # print(len(winner) - idx, v)
print(t)
