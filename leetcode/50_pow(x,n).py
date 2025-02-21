# https://leetcode.com/problems/powx-n/description/

def myPow(x, n):
    res =  1
    m = abs(n)
    while m:
        if m&1:
            res *= x
        x *= x
        m >>= 1
    if n < 0:
        return 1/res
    return res

x = 5
n = -4
print(myPow(x, n))