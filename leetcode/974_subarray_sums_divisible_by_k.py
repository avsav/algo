# https://leetcode.com/problems/subarray-sums-divisible-by-k/

from collections import defaultdict

def subarraysDivByK(nums, k):
    n = len(nums)
    prefix = prefixModK = res = 0
    hm = defaultdict(int)
    hm[0] = 1
    for num in nums:
        prefix += num
        prefixModK = prefix % k
        res += hm[prefixModK]
        hm[prefixModK] += 1

    return res


k1 = 2
nums1 = [1,3,5]
k2 = 5
nums2 = [4,5,0,-2,-3,1]
k3 = 9
nums3 = [5]
print(subarraysDivByK(nums2, k2))