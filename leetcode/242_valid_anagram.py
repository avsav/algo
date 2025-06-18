# https://leetcode.com/problems/valid-anagram/description/

from collections import defaultdict

def isAnagram(s, t):
    st = defaultdict(int)
    tt = defaultdict(int)
    for i in s:
        st[i] += 1
    for i in t:
        tt[i] += 1
    for key in st:
        if key not in tt or st[key] != tt[key]:
            return False
    for key in tt:
        if key not in st or st[key] != tt[key]:
            return False
    return True


s1 = "anagram"
t1 = "nagaram"
s2 = "rat"
t2 = "car"
s3 = "a"
t3 = "ab"
print(isAnagram(s3, t3))