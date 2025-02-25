# https://leetcode.com/problems/continuous-subarray-sum/description/

def checkSubarraySum(nums, k):
    n = len(nums)
    prev = 0
    curr = 0
    s = set()
    for i in range(n):
        prev = curr
        curr = (curr + nums[i]) % k
        if curr in s:
            return True
        s.add(prev)
    return False



k1 = 6
nums1 = [23,2,4,6,7]
nums2 = [23,2,6,4,7]
k2 = 13
nums3 = [23,2,6,4,7]
k3 = 7
nums4 = [23,2,4,6,6]
print(checkSubarraySum(nums1, k1))