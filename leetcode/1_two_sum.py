# https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if (nums[i] + nums[j] == target):
                return [i,j]
                

nums = [int(item) for item in input().split()]
target = int(input())
print(twoSum(nums, target))