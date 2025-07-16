# https://leetcode.com/problems/subsets-ii

def subsets(nums):
    n = len(nums)
    res = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & 1 << j:
                subset.append(nums[j])
        res.append(subset)

    return res



def subsetsWithDup(nums):
    res = []
    subset = []

    def backtrack(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        subset.append(nums[i])
        backtrack(i + 1)
        subset.pop()
        backtrack(i + 1)
    
    backtrack(0)

    return res


nums = [1,2,3]
print(subsets(nums))
print(subsetsWithDup(nums))