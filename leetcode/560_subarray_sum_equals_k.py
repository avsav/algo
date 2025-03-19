# https://leetcode.com/problems/subarray-sum-equals-k/description/

from collections import defaultdict

def subarraySum(nums, k):
    n = len(nums)
    hm = defaultdict(int)
    hm[0] = 1
    prefix = res = 0
    for i in range(n):
        prefix += nums[i]
        res += hm[prefix - k]
        hm[prefix] += 1

    return res


nums1 = [1,1,1]
k1 = 2
nums2 = [1,2,3]
k2 = 3
nums3 = [1,1,2,5]
k3 = 7
print(subarraySum(nums2, k2))