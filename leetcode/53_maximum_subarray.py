# https://leetcode.com/problems/maximum-subarray/description/?envType=problem-list-v2&envId=nb4ro6ft


def maxSubArray(nums):
    n = len(nums)
    prefix = subMax = nums[0]
    for i in range(1, n):
        prefix = max(prefix + nums[i], nums[i])
        if prefix >= subMax:
            subMax = prefix

    return subMax



nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [1]
nums3 = [5,4,-1,7,8]
nums4 = [-2, 1, 3]
print(maxSubArray(nums2))
