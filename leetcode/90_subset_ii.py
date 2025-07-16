# https://leetcode.com/problems/subsets-ii

def subsetWithDup1(nums):
    n = len(nums)
    res = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & 1 << j:
                subset.append(nums[j])
        subset.sort()       
        if subset not in res:
            res.append(subset)

    return res



def subsetsWithDup2(nums):
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


nums = [1,2,2,3]
print(subsets(nums))
print(subsetsWithDup(nums))