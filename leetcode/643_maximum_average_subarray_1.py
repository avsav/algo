# https://leetcode.com/problems/maximum-average-subarray-i/description/

def findMaxAverage(nums, k):
    n = len(nums)
    sum = 0
    for j in range(k):
        sum += nums[j]
    i = 1
    max = sum
    while(i + k <= n):
        sum = sum - nums[i - 1] + nums[i + k - 1]
        if sum > max: max = sum
        i += 1
    return max/k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))