# https://leetcode.com/problems/max-consecutive-ones/description/

def findMaxConsecutiveOnes(nums):
    n = len(nums)
    left = 0
    maxLen = 0
    for right in range(1, n):
        if nums[left] == 0:
            left += 1
        if nums[right] == 0:
            left = right

        maxLen = max(maxLen, right - left + 1)
    
    return maxLen


nums1 = [1,1,0,1,1,1]
nums2 = [1,0,1,1,0,1]
nums3 = [0,0,0,1,1,1,0,1,0,0,1,1]
print(findMaxConsecutiveOnes(nums3))