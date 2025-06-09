# https://leetcode.com/problems/isomorphic-strings/

from collections import defaultdict

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    ht1 = defaultdict(set)
    ht2 = defaultdict(set)
    for i in range(len(s)):
        ht1[t[i]].add(s[i])
        ht2[s[i]].add(t[i])
        if len(ht1[t[i]]) > 1 or len(ht2[s[i]]) > 1:
            return False

    return True


s1 = "foo"
t1 = "bar"
s2 = "egg"
t2 = "add"
s3 = "badc"
t3 = "baba"
s4 = "paper"
t4 = "title"
print(isIsomorphic(s3, t3))

    