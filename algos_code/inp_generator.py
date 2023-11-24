import random
from collections import defaultdict

def weighted_graph(num_nodes=1000, sparse=False):
    """Takes num_nodes and return n^2 dictionary with adjacency list and (cost, end) nodes"""
    nodes = list(range(num_nodes))
    random.shuffle(nodes)
    weighted_graph2 = defaultdict(list)
    # dense graph
    for n in nodes:
        so_far = {y for x,y in weighted_graph2[n]}
        nodes2 = [x for x in range(num_nodes) if x != n and x not in so_far]
        random.shuffle(nodes2)
        for n2 in (nodes2[:max(num_nodes // 10, 1)] if sparse else nodes2):
            cost = random.randint(1,num_nodes**2)
            weighted_graph2[n].append((cost, n2))
            weighted_graph2[n2].append((cost, n))
    return weighted_graph2

def rand_list(length=10):
    """ Returns random list of numbers 0 to n exclusive"""
    x = list(range(length))
    random.shuffle(x)
    return x