# https://leetcode.com/problems/first-bad-version/description/

def isBadVersion(n):
    pass

def firstBadVersion(n):
    low = 1
    high = n
    ans = 0
    while (low <= high):
        mi = (low + high) // 2
        if (isBadVersion(mi)):
            high = mi - 1
            ans = mi
        else:
            low = mi + 1
    return ans
