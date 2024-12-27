# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicates(nums):
    n = len(nums)
    k = 0
    left = 0
    for right in range(1, n):
        if nums[left] != nums[right]:
            left += 1
            nums[left], nums[right] = nums[right], nums[left]
            k += 1

    return k + 1

nums = [1,1,2]
print(removeDuplicates(nums))
