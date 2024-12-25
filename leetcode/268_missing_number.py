# https://leetcode.com/problems/missing-number/description/

def missingNumber(nums):
    n = len(nums)
    arr = (n + 1) * [0]
    for num in nums:
        arr[num] = 1
    for i in range(n + 1):
        if arr[i] < 1: return i


nums = [0, 1]
print(missingNumber(nums))
