# https://leetcode.com/problems/max-consecutive-ones/description/

def findMaxConsecutiveOnes(nums):
    n = len(nums)
    left = 0
    maxLen = 0
    for right in range(n):
        if nums[left] == 0:
            left += 1
            continue
        if nums[right] == 0:
            left = right

        maxLen = max(maxLen, right - left + 1)
    
    return maxLen


nums1 = [1,1,0,1,1,1]
nums2 = [1,0,1,1,0,1]
nums3 = [0,0,0,1,1,1,0,1,0,0,1,1]
nums4 = [0]
nums5 = [1]
nums6 = [0,0]
nums7 = [1,0]
print(findMaxConsecutiveOnes(nums5))