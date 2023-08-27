# Performance/Memory/Big O
# Deque
# Adv: for O(1) appending/pop from each end of list (impl as linkedlist), python list is array under hood, so prepening is O(n)
# Disadv: O(n) instert delete, memory overhead to store pointers O(2n), not designed for sorting/searching, synch issues if used in multi-threaded env
#
#
# Problem solving:
# if using map/dynamic prog check if map should be local to each recursive call (create empty each time) or global (don't need to pass if python)
# use deque() 
# When looking at sets of items with connection to other sets
# consider both approches, adding the items which are valid, or removing the items which aren't
# 
# 
# 
# 
# 
# 
# 
# 
#
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Syntax:
# format(num, "#038b")[2:] - converts number to binary string with leading zeros to "38" width
# bin(num) - converts integer:100 -> '0b1100100'
# Bitwise operators - & - AND, | - OR, ^ - XOR, ~ - NOT. a << n, a >> n, left/right shift n bits
# switch statement in python 3.10 onwards.
# match lang:
#     case "Python" | "Not python":
#         pass
#     case _:
#         pass
# print(f"{ins} is invalid")
# safe set remove (set.discard(), unsafe remove set.remove() (throws error if not in set))
# set.union(*list(could_be.values())) if you have dict of set values, then they need to be unioned first
# sortedKeyList = sorted(could_be.keys(), key=lambda s: len(could_be.get(s)))
# match lang:
#     case "Python" | "Not python":
#         pass
#     case _:
#         pass
# f-strings in python
# print(f"{ins} is invalid")
# 
# can use |= for set.union and &= for set.intersection() -= for set difference
# union/set over list just unpack so set.union(*some_list_of_sets)






# String syntax
# string.split(delimeters)
# string.strip(",.grt") - txt = ",,,,,rrttgg.....banana....rrr", removes leading/trailing characters, default is whitespace " "
# ",".joing(string)
# string.replace(",", "x")