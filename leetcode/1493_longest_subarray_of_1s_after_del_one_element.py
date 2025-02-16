# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/

def longestSubarray(nums):
    left = 0
    cz = 0
    maxi = 0
    n = len(nums)
    for right in range(n):
        if nums[right] == 0:
              cz += 1

        while cz > 1:
            if nums[left] == 0:
                cz -= 1            
            left += 1

        maxi = max(right - left, maxi)
         
    return maxi


nums = [0,1,1,1,0,1,1,0,1]
nums1 = [1,1,0,1]
nums2 = [0,0,1,1]
print(longestSubarray(nums2))