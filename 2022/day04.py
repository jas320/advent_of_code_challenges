from utils import loadInput, loadeg

lines = loadInput()
# lines = loadeg()
# slow solution, should check start and end indexes but this is faster
c = 0
for l in lines:
    p1,p2 = [list(map(int, x.split("-"))) for x in l.split(",")]
    a,b = set(range(p1[0], p1[1] + 1)), set(range(p2[0], p2[1] + 1))
    if len(a.intersection(b)) != 0:
        c += 1
print(c)
    