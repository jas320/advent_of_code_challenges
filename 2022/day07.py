from utils import loadInput


inputLines = loadInput()
base = {("/", ()):[]}
parents = [] # stack to keep track of directory, filled with names only
cd = "/"
for l in inputLines:
    l = l.split(" ")
    c = l[0]
    if c == "$":
        _,comm,*p = l
        if comm == "cd":
            if p[0] == "/":
                parents = []
                cd = "/"
            elif p[0] == "..":
                cd = parents.pop()
            else:
                # p[0] represent name
                parents.append(cd) # append current parent
                # print(parents)
                cd = p[0]
                if cd not in base:
                    base[(cd, tuple(parents))] = []
    else:
        type_, name = l
        if type_ == "dir":
            base[(cd, tuple(parents))].append(name)
        else:
            base[(cd, tuple(parents))].append(int(type_))
print(base)
sizes = {}
def calc_size(name, parents):
    t = 0
    key = (name, tuple(parents))
    for c in base[key]:
        if type(c) == int:
            t += c
        else:
            # print(name)
            parents.append(name)
            t += calc_size(c, parents)
    if len(parents) > 0:
        parents.pop()
    sizes[key] = t
    return t
calc_size("/", [])
print(sum([sizes[x] for x in sizes if sizes[x] <= 100_000]))
used = sizes[("/", ())]
unused = 70000000 - used
for x in sorted(sizes.values()):
    if x >= 30000000 - unused:
        print(x)
        break
        