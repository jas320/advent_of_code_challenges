class Node:
    def __init__(self, type, time):
        self.type = type
        self.time = time
    
    # assumption other is of correct type otherwise will throw error
    def __lt__(self, other):
        if self.time != other.time:
            return self.time < other.time
        else:
            return self.type < other.type

# idea: store tuples of differetn type of events and put into priority queue (heap)
# Node = (type of event, time of event)
# 0 - Turn on (events must be processed in this order)
# 1 - Bench
# 2 - Turn off
import heapq

# O(nlogn, O(n))
def sweep_line(lamps, points):
    events = []
    for a,b in lamps:
        events.append(Node(0, a))
        events.append(Node(2, b))
    for p in points:
        events.append(Node(1 ,p))
        
    heapq.heapify(events) # in place heapify using __lt__ operator to compare.
    c = 0
    out = []
    while events:
        node = heapq.heappop(events)
        match node.type:
            case 0:
                c += 1
            case 1:
                out.append(c)
            case _:
                c -= 1
    return out

# O(n^2), O(1)
def brute_force(lamps, points):
    return [sum([a <= p <= b for (a,b) in lamps]) for p in points]

# lamps = [[-3, 0], [-20, -3], [-10,10], [5,8]]
# points = [-3,3,1,7,5,10]
import random as r
import time
lamps = [sorted((r.randint(0,10), r.randint(0,10))) for _ in range(2*10 **5)]
points = [-3,1,3,5,7,10]

# print(lamps)
# print())
t1 = time.perf_counter()
res1 = brute_force(lamps, points)
t2 = time.perf_counter()
res2 = sweep_line(lamps, points)
t3 = time.perf_counter()

print(res1)
print(t2 - t1)
print(res2)
print(t3 - t2)
                



