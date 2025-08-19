# https://leetcode.com/problems/largest-number/description/?envType=problem-list-v2&envId=nb4ro6ft

from functools import cmp_to_key

def largestNumber(nums):
    n = len(nums)

    def compare(a, b):
        n = len(str(a))
        m = len(str(b))

        return 10**n * b + a - 10**m * a - b


    nums = sorted(nums, key=cmp_to_key(compare))
    res  = ""
    for i in range(n):
        res += str(nums[i])

    return res






nums1 = [2,10]
nums2 = [3,30,34,5,9]
print(largestNumber(nums2))
