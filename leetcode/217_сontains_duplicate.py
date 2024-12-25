# https://leetcode.com/problems/contains-duplicate/description/

from collections import defaultdict

def containsDuplicate(nums):
    #table = collection.defaultdict(int)
    hash_table = defaultdict(int)
    for num in nums:
        hash_table[num] += 1
        if hash_table[num] > 1: return True
    return False


nums = [1, 2, 3, 1]
print(containsDuplicate(nums))