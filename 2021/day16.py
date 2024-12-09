from utils import loadInput, loadeg
from collections import defaultdict, Counter, deque
import numpy as np
import math
import sys

inputLines = loadInput()
# inputLines = loadeg()
# print(inputLines)
line = inputLines[0]
n = 4
# groups = [line[i : i + n] for i in range(0, len(line), n)]
# line = line[:-3]
groups = [str(format(int(x, 16), "04b")) for x in line]
print(groups)
bits = "".join(groups)
print(bits)
# quit()
m = {1: 0} # used for keeping track of global version count

# assume header removed

def header(bits):
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    return version, type_id, bits[6:]

def packet(bits):
    if len(bits) == 0 or all([x == '0' for x in bits]):
        return 0, [], []
    version, type_id, rem = header(bits)
    print(f"version {version}, type_id {type_id}")
    m[1] += version
    if type_id == 4:
        bits_used, rem, values = literal(rem)
        res = values
        print("res", values)
    else:
        bits_used, rem, values = operator(rem)
        if type_id == 0:
            print ("summing", values)
            res = sum(values)
        elif type_id == 1:
            res = math.prod(values)
        elif type_id == 2:
            res = min(values)
        elif type_id == 3:
            res = max(values)
        elif type_id == 5:
            res = 1 if values[0] > values[1] else 0
        elif type_id == 6:
            res = 1 if values[0] < values[1] else 0
        elif type_id == 7:
            print("ready for", values)
            res = 1 if values[0] == values[1] else 0
        res = [res]
    # include header in returning bits used
    print("res returning", res)
    return bits_used + 6, rem, res

def literal(bits):
    start = 0
    total = []
    while True:
        temp = bits[start: start + 5]
        if len(temp) < 5:
            start += len(temp)
            break
        # print(temp)
        prefix, rest = temp[0], temp[1:]
        print(prefix, temp)
        total.append(rest)
        start += 5
        if prefix == '0':
            break
    bits_used = start
    total = "".join(total)
    literal_value = int(total, 2)
    print("literal:", total)
    print("literal value: ", literal_value)
    return bits_used, bits[start:], [literal_value] # convert to decimal

def operator(bits):
    length_type_id = bits[0]
    print(f"length type id {length_type_id}")
    vals = []
    if length_type_id == '0':
        length_sub_packets, rem = int(bits[1:16], 2), bits[16:]
        total = 0
        while total < length_sub_packets:
            sub_bits_used, rem,values = packet(rem)
            total += sub_bits_used
            vals += values
            if sub_bits_used == 0:
                break
            #TODO not sure about this
        return total + 15 + 1, rem, vals
    elif length_type_id == '1':
        #01010 = 10
        num_sub_packets, rem = int(bits[1:12], 2), bits[12:]
        total_packets = 0
        total = 0
        while total_packets < num_sub_packets:
            sub_bits_used, rem, values = packet(rem)
            print("values", values)
            total += sub_bits_used
            total_packets += 1
            vals += values
        print("vals", vals)
        return total + 11 + 1, rem, vals

bits_used ,rem, values = packet(bits)
print("bits_used:", bits_used, "rem: ", rem, "values", values)
print(m[1])

