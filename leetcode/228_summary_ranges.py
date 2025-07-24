# https://leetcode.com/problems/summary-ranges/

def summaryRanges1(nums):
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


def summaryRanges2(nums):
    res = []
    for num in nums:
        if res and res[-1][1] == num - 1:
            res[-1][1] = num
        else:
            res.append([num,num])

    return [f"{a}->{b}" if a != b else f"{a}" for a, b in res]



nums = [0, 2, 3, 4, 6, 8, 9]
print(summaryRanges2(nums))