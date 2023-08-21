
from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys
inputLines = loadInput()
# inputLines = loadeg()
# starts facing east , N,E,S,W,0,90,180,270
def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    angle = math.radians(angle)
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return round(qx), round(qy)

x,y,d = 0,0,90
wx,wy,wd = 10,1,90
for ins in inputLines:
    c, v = ins[0], int(ins[1:])
    match c:
        case "N":
            wy += v
        case "S":
            wy -= v
        case "E":
            wx += v
        case "W":
            wx -= v
        case "L":
            wx,wy = rotate((0,0),(wx,wy),v)
        case "R":
            wx,wy = rotate((0,0),(wx,wy),360 - v)
        case "F":
            x += (v * wx)
            y += (v * wy)
        case _:
            print(f"{ins} is invalid")
    print(x,y,ins)
    print(wx,wy)
print(x,y, abs(x) + abs(y))


                    
        