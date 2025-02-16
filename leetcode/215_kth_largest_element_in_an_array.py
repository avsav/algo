# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

#from random import randrange
from collections import defaultdict

def findKthLargest(nums, k):
    #qsort(nums, 0, len(nums) - 1)
    max = -10**10
    for num in nums:
        if num > max:
            max = num
    ht = defaultdict(int)
    #ht = [0] * len(nums)
    for num in nums:
        d = max - num
        ht[d] += 1
    d = cnt = 0
    while cnt < k:
        cnt += ht[d]
        d += 1
    return max - d + 1


"""
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
"""

nums = [3,2,3,1,2,4,5,5,6]
k = 4
#qsort(nums, 0, len(nums) - 1)
print(nums)
print(findKthLargest(nums, k))