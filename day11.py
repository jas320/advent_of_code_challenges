from utils import loadInput
import numpy as np

inputLines = loadInput()
divs = [2,3,5,7,11,13,17,19]
# divs = [23,19,13,17]
def parse(str, m):
    strs = list(map(lambda x : x.split(" "), str))
    monkey_n = int(strs[0][1][0])
    start_items = list(map(lambda x : x.replace(",", "").replace(" ", ""), strs[1][4:]))
    start_items = list(map(int, start_items))
    # new = old * 19 (lambda from old to new)
    snd = lambda x : x if strs[2][-1] == "old" else int(strs[2][-1])
    op = lambda x : sum([x, snd(x)]) if strs[2][-2] == "+" else np.prod([x,snd(x)])
    # op = lambda x : sum([x, snd(x)]) if strs[2][-2] == "+" else snd(x)
    # returns 2 if val divisilbe by 23 else
    vs = [int(strs[3:][i][-1]) for i in range(3)]
    tst = lambda x : vs[1] if x % vs[0] == 0 else vs[2]
    m[monkey_n] = {"items" : start_items, "op" : op, "tst" : tst, "insp": 0}

def round(num_rounds, m, lcm):
    for j in range(num_rounds):
        for i in range(max(m) + 1):
            curr = m[i]
            for wl in curr["items"]:
                # print(wl)
                curr["insp"] += 1
                wl = curr["op"](wl)
                wl %= lcm
                throw_to = curr["tst"](wl)
                m[throw_to]["items"].append(wl)
            curr["items"] = []
    s = sorted([m[i]["insp"] for i in range(max(m) + 1)], reverse=True)
    # print([m[i]["items"] for i in range(max(m) + 1)])
    # print(max(m))
    print(s)
    return s[0] * s[1]

m = {}
lcm = 1
for x in divs:
    lcm *= x

for i in range(0, len(inputLines), 7):
    parse(inputLines[i : i + 7], m)
# for key in m.keys():
#     print(m[key])

print(round(10000, m, lcm))
    


