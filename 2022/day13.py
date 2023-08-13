from utils import loadInput
import functools

def rec(x, y):
    # print("comparing", x, y)
    if isinstance(x, int) and isinstance(y, int):
        return True if x < y else (False if x > y else None)
    elif isinstance(x, list) and isinstance(y, list):
        for a,b in zip(x,y):
            res = rec(a,b)
            if res is not None:
                return res
        return True if len(x) < len(y) else (False if len(x) > len(y) else None)
    else:
        return rec([x],y) if isinstance(x, int) else rec(x, [y])
def wrap(a, b):
    r = rec(a,b)
    return 0 if r is None else (1 if r else -1)

inp = loadInput()
inp = [eval(x) for x in inp if x != ""]
a,b = [[2]], [[6]]
inp.extend([a,b])
inp = sorted(inp, key=functools.cmp_to_key(wrap), reverse=True)
print((inp.index(a) + 1) * (inp.index(b) + 1))

        