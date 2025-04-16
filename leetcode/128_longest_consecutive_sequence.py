# https://leetcode.com/problems/longest-consecutive-sequence/description/

from collections import defaultdict

def longestConsecutive(nums):
    nums = set(nums)
    maxLen = 0
    for num in nums:
        if num - 1 not in nums:
            nyam = num + 1
            while nyam in nums:
                nyam += 1
            maxLen = max(maxLen, nyam - num)
    return maxLen


nums1 = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
nums3 = [1,0,1,2]
print(longestConsecutive(nums1))