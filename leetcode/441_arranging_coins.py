# https://leetcode.com/problems/arranging-coins/description/

def arrangeCoins(n):
    def f(k):
        return k * (k + 1) // 2 

    lo = 1
    hi = n
    ans = 0
    while (lo <= hi):
        mi = lo + (hi - lo) // 2
        if (f(mi) > n):
            hi = mi - 1
        elif (f(mi) < n):
            lo = mi + 1
            ans = mi 
        else:
            return mi
    return ans


n = 6
print(arrangeCoins(n))
