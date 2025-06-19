# https://leetcode.com/problems/remove-element/description/

def removeElement(nums, val):
    n = len(nums)
    k = 0
    for i in range(n):
        if nums[i] == val:
            k += 1
    left = 0
    for right in range(1, n):
        if nums[left] == val and nums[right] != val:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] != val:
            left += 1
    return len(nums[:(n - k)])


nums1 = [3,2,2,3]
val1 = 3
nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
print(removeElement(nums2, val2))