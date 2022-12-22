import os
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

# def grid(h, w):
#     return [[str[i][j] for j in range(w)] for i in range(h)]