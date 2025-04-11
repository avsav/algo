# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/

def numOfSubarrays(arr):
    mod = 10**9 + 7
    prefix = ns = 0
    odd = 0 
    even = 1
    for num in arr:
        prefix += num
        if prefix % 2:
            odd += 1
            ns += even
        else:
            even += 1
            ns += odd
    return ns % mod


arr = [2,4,6]
print(numOfSubarrays(arr))
