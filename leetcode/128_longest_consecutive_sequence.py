# https://leetcode.com/problems/longest-consecutive-sequence/description/

from collections import defaultdict

def longestConsecutive(nums):
    n = len(nums)
    nums = set(nums)
    hm = defaultdict(list)
    for num in nums:
        hm[num] = num + 1
    return hm


nums1 = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
nums3 = [1,0,1,2]
print(longestConsecutive(nums3))