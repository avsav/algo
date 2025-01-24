# https://leetcode.com/problems/number-of-1-bits/description/

def hammingWeight(n: int) -> int:
    mask = 1
    cnt = 0
    while n:
        if mask & n:
            cnt += 1
        n = n >> 1
    return cnt

n = 13
print(hammingWeight(n))