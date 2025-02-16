# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

from random import randrange


def findKthLargest(nums, k):
    qsort(nums, 0, len(nums) - 1)
    return nums[len(nums) - k]

def rand_partition(nums, a, b):
    n = randrange(a, b + 1)
    nums[n], nums[b] = nums[b], nums[n]
    pivot = nums[b]
    left = a - 1
    for right in range(a, b):
        if nums[right] <= pivot:
            left += 1
            nums[left], nums[right] = nums[right], nums[left]
    nums[left + 1], nums[b] = nums[b], nums[left + 1]
    return left + 1

def qsort(nums, a, b):
    if a < b:
        pivot = rand_partition(nums, a, b)
        qsort(nums, a, pivot - 1)
        qsort(nums, pivot + 1, b)


nums = [2,8,7,1,3,5,6,4]
qsort(nums, 0, len(nums) - 1)
print(nums)
print(findKthLargest(nums, 2))