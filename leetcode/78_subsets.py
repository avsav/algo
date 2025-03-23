# https://leetcode.com/problems/subsets/description/

def subsets(nums):
    n = len(nums)
    subset = []
    res = []

    def backtracking(index):
        if index >= n:
            res.append(subset.copy())
            return
        
        subset.append(nums[index])
        backtracking(index + 1)

        subset.pop()
        backtracking(index + 1)

    backtracking(0)

    return res



nums1 = [1,2]
nums2 = [0]
print(subsets(nums1))

