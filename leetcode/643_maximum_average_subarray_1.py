# https://leetcode.com/problems/maximum-average-subarray-i/description/

def findMaxAverage(nums, k):
    n = len(nums)
    i = 0
    max = -10**10
    while(i + k <= n):
        sum = 0
        for j in range(i, i + k):
            sum += nums[j]
        if sum > max: max = sum
        i += 1
    return max/k

nums = [5]
k = 1
print(findMaxAverage(nums, k))