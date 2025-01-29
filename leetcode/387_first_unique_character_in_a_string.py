# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import defaultdict

def firstUniqChar(s):
    hash_table = defaultdict(int)

    for symb in s:
        hash_table[symb] += 1

    char = ""
    for key, value in hash_table.items():
        if value == 1:
            char = key
            break
        
    if not char:
        return -1
    
    return s.find(char)


s = "aabb"
print(firstUniqChar(s))