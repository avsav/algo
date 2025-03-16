# https://leetcode.com/problems/group-anagrams/description/

from collections import defaultdict

def groupAnagrams(strs):
    ht = defaultdict(list)
    res = []
    for str in strs:
        sort_str = ''.join(sorted(str))
        ht[sort_str].append(str)
    for v in ht.values():
        res.append(v)
    return res

strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]
print(groupAnagrams(strs3))