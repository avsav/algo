# https://leetcode.com/problems/is-subsequence/description/

def isSubsequence(s, t):
    left = 0
    n = len(t)
    if len(s) == 0:
        return True
    for right in range(n):
        if len(s) != 0 and t[right] == s[left]:
            left += 1
        if left == len(s):
            return True
    return False

s = "b"
t = "c"
print(isSubsequence(s, t))
