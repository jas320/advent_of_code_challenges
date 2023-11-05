#!/bin/python3

import math
import os
import random
import re
import sys



#!/bin/python3

import math
import os
import random
import re
import sys
import requests

#
# Complete the 'getUserTransaction' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER uid
#  2. STRING txnType
#  3. STRING monthYear
#
#  https://jsonmock.hackerrank.com/api/transactions/search?userId=
#  https://jsonmock.hackerrank.com/api/transactions/search?userId=uuid&page=5
#
from datetime import datetime
import calendar
url = "https://jsonmock.hackerrank.com/api/transactions/search?userId="
page = "&page="
def getUserTransaction(uid, txnType, monthYear):
    input = monthYear
    format = '%m-%Y'
    date1 = datetime.strptime(input, format)
    print("inp date", date1.date())
    num_records = 0
    print("url", url + str(uid) + page + "0")
    r = requests.get(url + str(uid) + page + "0").json()
    mpages = r['total_pages']
    t = 0.000
    amounts = [] # assume from 1 - 4
    print("mpages", mpages)
    seen = set()
    for page_num in range(mpages + 1):
        r = requests.get(url + str(uid) + page + str(page_num)).json()
        data = r['data']
        # print(r)
        for json in data:
            if json['id'] in seen:
                continue
            seen.add(json['id'])
            # print("full", json)
            date2 = datetime.utcfromtimestamp(json['timestamp']//1000)
            # print("date1", date1.date(), "date2", date2.date())
            if date1.date().month == date2.date().month and date1.date().year == date2.date().year:
                    print("year and month matched", date1.date(), date2.date())
                    v = float(json['amount'][1:].replace(",","_"))
                    print("type", json['txnType'], "input_type", txnType)
                    if json['txnType'] == txnType:
                        print(json['amount'], "converted_val", v)
                        t += v
                        amounts.append((json['id'], v))
    print("final amounts:", amounts)
    if len(amounts) == 0:
        return [-1]
    print(t)
    avg = t / len(amounts)
    print(avg)
    res = sorted([id_ for (id_, v) in amounts if v * len(amounts) > t])
    return res if res != [] else [-1]
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    uid = int(input().strip())

    txnType = input()

    monthYear = input()

    result = getUserTransaction(uid, txnType, monthYear)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


from datetime import datetime
 
 
timestamp = 1567374731671 // 1000
dt_obj = datetime.fromtimestamp(timestamp)
 
print("date_time:",dt_obj)
print("type of dt:",type(dt_obj))
























# given used [1,2,3,1] and total [4,3,3,2], find minimum number of final partitions ()
# greedy algorithm works because don't care about number of moves

def compaction_algo(used, total):
    t = sum(used)
    c = 0
    total.sort()
    while t > 0:
        next = total.pop()
        c += 1
        t -= next
        print(f"{c} move into {next}")
    return c
# print(compaction_algo([3,2,1,3,1], [3,5,3,5,5]))

# takes list of integers and balances them to all be above 100 in efficient way (maintains two stacks)
# O(n), O(n)
def split_100(tuples):
    stack_take = [(k,v) for k,v in tuples if v > 100]
    stack_add = [(k,v) for k,v in tuples if v < 100]
    
    while len(stack_take) > 0 and len(stack_add) > 0:
        k, v = stack_take[-1]
        k2, v2 = stack_add[-1]
        over = v - 100
        under = 100 - v2
        
        # assuming if they are popped no need to update
        if over > under:
            amount = under
            stack_take[-1] = (k, v - amount)
            stack_add.pop()
        elif over == under:
            amount = under
            stack_take.pop()
            stack_add.pop()
        else:
            amount = over
            stack_add[-1] = (k2, v2 + amount)
            stack_take.pop()
        print(f" {amount} {k} -> {k2}")
        # print(stack_take, stack_add)
    if len(stack_add) > 0:
        print("Did not complete")

t = [60,70,80,130,110,150]
t2 = [80,80]
t3 = [110,110]
t4 = [50,110,120]
t5 = [50,130,130]
t6 = [1000,1,1,1,1,1]
l = ["a","b","c","d","e","f"]
# for x in [t, t2, t3, t4, t5, t6]:
#     split_100(list(zip(l, x)))

class Node:
    def __init__(self, sub):
        self.subtrees = sub
    
def solution(tree):
    _, _, n = solution2(tree, 0)
    return n

def solution2(tree, n):
    # Implement your solution here
    sub_trees = tree.subtrees
    if sub_trees == []:
        return True, 1, n + 1

    total = 0
    allBalanced = True
    start_size = None
    for x in sub_trees:
        (isBalanced, size, n) = solution2(x, n)
        if start_size is None:
            start_size = size
        else:
            if size != start_size:
                allBalanced = False
        total += size
    return allBalanced, 1 + total, n + 1 if allBalanced else n


t1 = Node([
    Node([
        Node([]),
        Node([])]),
    Node([
        Node([
            Node([
                Node([]),
                Node([])
            ])
        ])
    ])
])
# print(solution(t1))



