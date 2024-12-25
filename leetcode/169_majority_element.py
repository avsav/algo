# https://leetcode.com/problems/majority-element/description/

from collections import defaultdict

def majorityElement(nums):
    n = len(nums) // 2
    hash_table = defaultdict(int)
    for num in nums:
        hash_table[num] += 1
        if (hash_table[num] > n):
            return num
        

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))