# https://leetcode.com/problems/destination-city/description/

from collections import defaultdict

def destCity(paths):
    n = len(paths)
    res = ""
    ht = defaultdict(str)
    for i in range(n):
        ht[paths[i][0]] = paths[i][1]
        ht[paths[i][1]] += ""
    for key in ht:
        if ht[key] == "":
            res = key
    return res


paths1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
paths2 = [["B","C"],["D","B"],["C","A"]]

print(destCity(paths2))
