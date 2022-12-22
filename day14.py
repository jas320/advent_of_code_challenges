from utils import loadInput, loadeg


inputLines = loadInput()
# inputLines = loadeg()

h,w = 5000,5000
g = [["." for j in range(w)] for i in range(h)]
inp = [l.replace(" -> ", ",").split(",") for l in inputLines]
inp = [list(map(int, x)) for x in inp]
high_y = -1
for l in inp:
    print(l)
    for i in range(0, len(l) - 2, 2):
        x1,y1, x2, y2 = l[i],l[i +1],l[i + 2],l[i + 3]
        high_y = max(max(high_y, y1), y2)
        for k in range(min(y1,y2), max(y1,y2) + 1):
            for m in range(min(x1,x2), max(x1,x2) + 1):
                g[k][m] = "#"
                # print(k,m)
g[0][500] = "+"
for j in range(h):
    g[high_y + 2][j] = "#"
i,j = 0,500
r = 0
print(high_y)
while True:
    if g[i + 1][j] != "#" and g[i + 1][j] != "o":
        i = i + 1
    elif g[i + 1][j - 1] != "#" and g[i + 1][j - 1] != "o":
        i = i + 1
        j = j - 1
    elif g[i + 1][j + 1] != "#" and g[i + 1][j + 1] != "o":
        i = i + 1
        j = j + 1
    else:
        # print(i,j)
        g[i][j] = "o"
        r += 1
        #settle
        if (i,j) == (0,500):
            print(r)
            break
        i,j = 0,500
# print(r)
# for l in g:
#     print("".join(l))