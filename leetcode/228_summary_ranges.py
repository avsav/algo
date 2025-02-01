# https://leetcode.com/problems/summary-ranges/

def summaryRanges(nums):
    if not nums:
        return []
    n = len(nums)
    res = []
    left = 0
    for right in range(1, n + 1):
        if right == n or nums[right] - nums[right - 1] != 1: 
            if nums[left] == nums[right - 1]:
                res.append(f"{nums[left]}")
            else:
                res.append(f"{nums[left]} -> {nums[right - 1]}")
            if right < n:
                left = right

    return res

nums = [0, 2, 3, 4, 6, 8, 9]
print(summaryRanges(nums))