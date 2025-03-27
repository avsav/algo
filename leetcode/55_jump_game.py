# https://leetcode.com/problems/jump-game/description/

def canJump(nums):
    n = len(nums)
    prev = next = nums[0]
    for i in range(1, n - 1):
        if i <= prev:
            next = max(prev, i + nums[i])
            prev = next
    
    if next < n - 1:
        return False

    return True



nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]
nums3 = [2,0,0]
print(canJump(nums2))