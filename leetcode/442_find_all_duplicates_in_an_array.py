# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

def findDuplicates(nums):
    n = len(nums)
    ht = [0] * (n + 1)
    res = []
    for num in nums:
        ht[num] += 1
        if ht[num] > 1:
            res.append(num)
    return res

nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))

