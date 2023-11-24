import random
# dfs - iterative solutions
m = {1: [2,3,4],
     2: [1,3,4,5],
     3: [1,2,4,5,6],
     4: [1,2,3],
     5: [2,3],
     6: [3,7],
     7: []
         }

# tree no cycle (modify to add cycle)
m2 = {1: [2,3],
      2: [1,4,5],
      3: [1,6,7],
      4: [2],
      5: [2],
      6: [3],
      7: [3]}

# directed graph no cycle
m3 = {1:[2,4],
      2:[3,5],
      3:[4],
      4:[5],
      5:[]
}

#O(V + E), O(1)
def dfs(root):
    seen = {root}
    stack = [root]
    while stack:
        curr = stack.pop()
        # curr = stack.popleft() for bfs
        # do stuff with curr here 
        print(curr)
        ns = m[curr] if curr in m else []
        for node in ns:
            if node not in seen:
                seen.add(node)
                stack.append(node)

# example of use, check cycles undirected graph - (no double linkes e.g only one link allowed between two nodes.)
#O(V + E), O(V)
def cycle_undir(root, m):
    seen = {root}
    stack = [root]
    parent = {root: None}
    while stack:
        curr = stack.pop()
        print(curr, "parent:", parent[curr])
        ns = m[curr] if curr in m else []
        for node in ns:
            if node not in seen:
                parent[node] = curr
                seen.add(node)
                stack.append(node)
            else:
                if node in parent and parent[curr] != node:
                    return True
    return False
# print(cycle_dir(1, m2))
# print(cycle_undir(1, m3))

# Iterative - Kahns algorithm, topological sort:
# if it successfully removes all vertices from the graph its a Directed Acylcial Graph (no cycle). If there are
# remaining vertices with in-degrees > 0, it indicates at least 1 cycle.
# Hence if we cannot get all vertices in topological sorting, must be at least one cycle.
# Recursive - Check if visited node in curr path (recursion stack)
from collections import deque
def cycle_dir(m):
    inDegree = {k : 0 for k in m}
    q = deque()
    visited = 0

    # Calculate in-degree of each vertex
    for k in m:
        for n in m[k]:
            inDegree[n] += 1

    # Enqueue vertices with 0 in-degree
    for k,v in inDegree.items():
        if v == 0:
            q.append(k)

    # BFS traversal
    while q:
        u = q.popleft()
        visited += 1

        # Reduce in-degree of adjacent vertices
        for v in m[u]:
            inDegree[v] -= 1
            # If in-degree becomes 0, enqueue the vertex
            if inDegree[v] == 0:
                q.append(v)

    return visited != len(m)  # If not all vertices are visited, there is a cycle
# print(cycle_dir(m2))

m4 = {1: [8,7,6], 2:[8,7,5],3:[8,6,5],4:[7,6,5],8:[3,2,1],7:[4,2,1],6:[4,3,1],5:[2,3,4]}
# If vertices are ordered according to degrees, guranteed to never use more than d + 1 colours where d is
# the maximum degree of a vertex in the graph. Determing if graph can be k =2 coloured is solved using dfs in O(n) time.
# Optimisation - DSatur, next uncoloured node to chose is one with highest num of colours in its neighbourhood.
# Uses - where two obj need to use a resource at the same time. (slot)e.g. register allocation, course scheduling - vertex for every job
# and an edge for conflicting pairs of jobs.
# O(V^2 + E), O(k) where k is the number of colours required.
def graph_colouring(m):
    vertices = list(m.keys())
    # random.shuffle(vertices)
    mapping = {}
    colours = []
    next_col = 0
    for v in vertices:
        # create set of mapping of neighbours
        ns = {mapping[x] for x in m[v] if x in mapping}
        for c in colours:
            if c not in ns:
                mapping[v] = c
                break
        if v not in mapping:
            colours.append(next_col)
            mapping[v] = next_col
            next_col += 1
    print("colours", set(mapping.values()))
    return mapping

# print(m4)
# print(graph_colouring(m4))

import heapq
from heapdict import heapdict
from collections import defaultdict
weighted_graph = {1:[(3,2),(5,3),(4,4)], 2:[(3,1),(4,3)],3:[(5,1),(4,2),(2,4)],4:[(4,1),(2,3)]}

import inp_generator as gen

weighted_graph2 = gen.weighted_graph(1000)
# -- WEIGHTED GRAPHS --
""" When networks have a cost associated with each arc e.g distance or time for transport network
MST - Spanning tree where sum of weights is minimum.
Uses - cheapest network connecting all cities, maximum flow through network"""
""" Prim's algorithm - keeps pq of adj items to pick from next and add to tree"""
# O(ElogV), O(V)
def minimum_spanning_tree_pq(m):
    start = list(m.keys())[0]
    h = heapdict()
    t = 0
    key = {x : float('inf') for x in m.keys()}
    h[start] = 0
    parent = {start: None}
    tree = {}
    while len(h) > 0:
        # get smallest weighted arc
        (start, cost) = h.popitem()
        t += cost
        tree[start] = True
        # add neighbours of min_value "end" arc
        for cost, end in m[start]:
            if end not in tree:
                if cost < key[end]:
                    # decrease key of h[end]
                    h[end] = cost
                    key[end] = cost
                    parent[end] = start
    print("Total cost is :", t)
    return parent

# O(V^2), O(V)   
def minimum_spanning_tree_classic(m):
    start =list(m.keys())[0]
    adj = {x for cost,x in m[start]}
    dist = {k : float('inf') for k in m.keys()}
    seen = {start}
    t = 0
    for cost,n in m[start]:
        if n not in seen:
            if cost < dist[n]:
                adj.add(n)
                dist[n] = cost
    while len(seen) < len(m.keys()):
        # print(seen)
        # print(dist, "adj", adj)
        min_node = min(adj, key= lambda x : dist[x])
        seen.add(min_node)
        adj.remove(min_node)
        t += dist[min_node]
        for cost,n in m[min_node]:
            if n not in seen:
                if cost < dist[n]:
                    adj.add(n)
                    dist[n] = cost
    print(t)
    return
import time
# print(weighted_graph2)
# t1 = time.time()
# minimum_spanning_tree_pq(weighted_graph2)
# t2 = time.time()
# minimum_spanning_tree_classic(weighted_graph2)
# t3 = time.time()
# print(t2 -t1)
# print(t3 - t2)                    

def shortest_path(start, end, m):
    pass

def shortest_path_heuristic(start, end, m):
    pass

def matrix_multiplication_optimised(m1, m2):
    pass



# Helper that merges two list, a and b are both sorted.
# O(n), O(n)
def merge_sorted(a, b):
    i,j = 0,0
    out = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out

nums = gen.rand_list(400_000)

# Out of place algorithm for sorting numbers using divide and conquer approach, has average and worst case
# Uses - database join queries, sorting linked lists O(1) extra space, where O(nlogn) is always required as worst case.
# O(nlogn), O(n) as have to store array to return.
def merge_sort(nums):
    if len(nums) == 1:
        return nums
    else:
        mid = len(nums) // 2
        l, r = merge_sort(nums[:mid]), merge_sort(nums[mid:])
        return merge_sorted(l, r)

# Non recursive merge sorted using deque to combine the sorted lists in a queue.
# Around 10% slower than merge_sort_recur for 400_000 elements
# O(nlogn), O(n) 
def merge_sort_iter(nums):
    queue = deque()
    for item in nums:
        queue.append([item])

    while len(queue) > 1:
        merged = merge_sorted(queue.popleft(), queue.popleft())
        queue.append(merged)
    return queue[0]

# In place sorting algorithm that calculates a pivot (random or median of 3), then splits the
# list either side if they are > or < the pivot. Continue until ordered. If list is likely to have sorted sequences
# use middle pivot to improve divisons.
# Uses - where memory is limited, where a stable comparison is not needed (simple algorithm is not stable)
# O(nlogn), O(1) - random pivot reduces n^2 worst case.
def quick_sort(nums, i, j, f):
    if i >= j or i < 0 or j > len(nums) - 1:
        return
    v = nums[f(i, j)]
    orig_i = i
    orig_j = j
    while i < j:
        # print(v, nums[i], nums[j] ,nums)
        if nums[i] >= v and nums[j] <= v:
            nums[i], nums[j] = nums[j], nums[i]
            if nums[i] == nums[j]:
                j -= 1
        elif nums[i] < v:
            i += 1
        elif nums[j] > v:
            j -= 1
        elif nums[i] == v:
            i += 1
        elif nums[j] == v:
            j -= 1
    while i > orig_i and nums[i] == v:
        i -= 1
    while j < orig_j and nums[j] == v:
        j += 1
    quick_sort(nums, orig_i, i - 1, f)
    quick_sort(nums, j + 1, orig_j, f)
    return

def quick_sort_middle(nums):
    quick_sort(nums, 0, len(nums) - 1, lambda a,b: (a + b) // 2)

def quick_sort_random(nums):
    quick_sort(nums, 0, len(nums) - 1, lambda a,b: random.randint(a,b))


"""
Modern Fischer-Yates in-place shuffle for shuffling finite sequence.
- Unbiased permutation so every permutation is equally likely, n! options.
- Optimal time and space complexity
- If want to parallelize, use sorting shuffle (assign random index to value and then sort in O(n))
  using radix sort. However this uses O(n) memory.
- pseudorandom number generators can only produce as many interal states as they represnet.
  so a 32 bit can only produce 2^32 < 2^225.6 (52!) reuqired for shuffling 52 cards.
"""
# O(n^2), O(1)
def random_shuffle(nums):
    random.shuffle()

def init_random_shuffle(size):





 