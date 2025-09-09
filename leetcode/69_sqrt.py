# https://leetcode.com/problems/sqrtx/description/?envType=problem-list-v2&envId=nb4ro6ft

def mySqrt(x):
    left = 0
    right = x
    
    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        elif mid * mid < x:
            left = mid + 1
        else:
            return mid
    return right


x1= 256
x2 = 13
x3 = 1
x4 = 0
print(mySqrt(x2))
