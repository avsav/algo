# https://leetcode.com/problems/running-sum-of-1d-array/description/

def runningSum(nums):
    n = len(nums)
    prefix = 0
    res = []
    for i in range(n):
        prefix += nums[i]
        res.append(prefix)

    return res


nums1 = [1,2,3,4]
nums2 = [1,1,1,1,1]
nums3 = [3,1,2,10,1]
print(runningSum(nums3))