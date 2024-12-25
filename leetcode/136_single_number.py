# https://leetcode.com/problems/single-number/description/

from collections import defaultdict

def singleNumber(nums):
    table = defaultdict(int)
    for num in nums:
        table[num] += 1

    for i in table:
        if table[i] == 1: return i


nums = [1]
print(singleNumber(nums))
