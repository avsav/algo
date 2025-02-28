# https://leetcode.com/problems/permutation-in-string/

from collections import defaultdict

def checkInclusion(s1, s2):
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for l in s1:
        d1[l] += 1
    for l in s2:
        d2[l] += 1       
        
    for d in d1:
        if d2[d] < d1[d]:
            return False   
        
    n1 = len(s1)
    n2 = len(s2)
    k = 0
    while k + n1 <= n2:
        if metric(s1, s2[k:k+n1]):
            return True
        k += 1

    return False


def metric(s1, s2):
    n = len(s1)
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for l in s1:
        d1[l] += 1
    for l in s2:
        d2[l] += 1  
    for d in d1:
        if d1[d] != d2[d]:
            return False
    return True    


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))