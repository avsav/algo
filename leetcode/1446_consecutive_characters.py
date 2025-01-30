# https://leetcode.com/problems/consecutive-characters/

from collections import defaultdict

def maxPower(s):
    n = len(s)
    cnt = maks = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            cnt += 1
            maks = max(maks, cnt)
        else:
            cnt = 1
    return maks
    

s1 = "leetcode"
s2 = "abbcccddddeeeeedcba"
s3 = "tourist"
print(maxPower(s1))