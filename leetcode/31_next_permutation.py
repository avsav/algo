# https://leetcode.com/problems/next-permutation/


def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = i + 1
        while j < n and nums[i] < nums[j]:
            j += 1
        j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        rev(nums, i + 1, n - 1)
    else:
        rev(nums, 0, n - 1)

    return nums


def rev(nums, start, end):
    left = start
    right = end 
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


nums1 = [1,2,3]
nums2 = [1,1,5]
nums3 = [1,5,8,4,7,6,5,3,1]
nums4 = [9,5,4,3,1]
nums5 = [3,2,1]
nums6 = [5,1,1]
nums7 = [1]
#print(rev(nums5, 0, len(nums1) - 1))
print(nextPermutation(nums1))
