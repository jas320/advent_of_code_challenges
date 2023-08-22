import os,math
def loadInput(fileName="input.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()
def loadeg(fileName="example.txt"):
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, fileName)) as file:
        return file.read().splitlines()
    
def grid(str):
    '''
    Convert n x m grid of items into list of lists
    '''
    h,w = len(str), len(str[0])
    return [[str[i][j] for j in range(w)] for i in range(h)]

def xy_cors(keys):
    y1,y2,x1,x2 = min(keys, key=lambda x : x[0])[0], max(keys, key=lambda x : x[0])[0], min(keys, key=lambda x : x[1])[1], max(keys, key=lambda x : x[1])[1]
    return y1, y2, x1, x2

def non_recursive_dfs(graph, start_vertex):
    stack = [start_vertex] # also can use collections.deque with appendleft, optimised for O(1) append and pop
    visited = [False] * len(graph) # if using indexes/array otherwise use set()

    while stack:
        vertex = stack.pop()

        if not visited[vertex]:
            visited[vertex] = True
            process_vertex(vertex) # operations to perform on vertex

            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    stack.append(neighbor)

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    For clockwis use negative angle (visa versa)
    The angle should be given in radians.
    """
    angle = math.radians(angle) # 
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return round(qx), round(qy)