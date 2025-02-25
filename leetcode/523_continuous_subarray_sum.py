# https://leetcode.com/problems/continuous-subarray-sum/description/

def checkSubarraySum(nums, k):
    n = len(nums)
    left = 0
    prefix = 0
    for right in range(n):
        if nums[right] > k:
            left = right + 1
        if nums[right] <= k:
            prefix += nums[right]
            while prefix > k and right - left + 1 >= 2:
                prefix -= nums[left]
                left += 1
                if prefix == k:
                    return True
    return False



k1 = 6
nums1 = [23,2,4,6,7]
nums2 = [23,2,6,4,7]
k2 = 13
nums3 = [23,2,6,4,7]
k3 = 7
nums4 = [23,2,4,6,6]
print(checkSubarraySum(nums4, k3))