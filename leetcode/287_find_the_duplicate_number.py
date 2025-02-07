# https://leetcode.com/problems/find-the-duplicate-number/description/

def findDuplicate(nums):
    n = len(nums)
    ht = [0] * n

    for num in nums:
        ht[num] += 1
        if ht[num] > 1:
            return num
    
nums = [1,3,4,2,2]
print(findDuplicate(nums))