# https://leetcode.com/problems/squares-of-a-sorted-array/description/

from random import randrange

def sortedSquares(nums):

    def partition(nums, l, r):
        k = randrange(l, r + 1)
        nums[k], nums[r] = nums[r], nums[k]
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def quicksort(nums, l, r):
        if l < r:
            pivot = partition(nums, l, r)
            quicksort(nums, l, pivot - 1)
            quicksort(nums, pivot + 1, r)

    for i in range(len(nums)):
        nums[i] *= nums[i]

    quicksort(nums, 0, len(nums) - 1)

    print(nums)


nums = [-4, -1, 0, 3, 10]
sortedSquares(nums)