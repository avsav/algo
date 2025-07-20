# https://leetcode.com/problems/subsets-ii

def subsetsWithDup1(nums):
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
    n = len(nums)
    nums.sort()
    
    subset = []
    res = []

    def backtrack(i):
        if i == n:
            res.append(subset[::])
            return
        subset.append(nums[i])
        backtrack(i + 1)
        subset.pop()
        while i + 1 < n and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1)
    
    backtrack(0)


    return res


nums = [1,2,2,3]
#print(subsetsWithDup1(nums))
print(subsetsWithDup2(nums))