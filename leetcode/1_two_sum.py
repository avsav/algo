# https://leetcode.com/problems/two-sum/description/

from collections import defaultdict

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if (nums[i] + nums[j] == target):
                return [i,j]
                

def twoSum2(nums, target):
    n = len(nums)
    d = defaultdict(int)

    for i in range(n):
        d[nums[i]] = i

    for i in range(n):
        compl = target - nums[i]
        if compl in d and i != d[compl]:
            return [i, d[compl]]
    
    return []
            




nums1 = [1,5,7,2,4]
target1 = 3
nums2 = [2,7,11,15]
target2 = 9
nums3 = [3,2,4]
target3 = 6
nums4 = [3,3]
target4 = 6
print(twoSum2(nums3, target3))