def searchInsert(nums, target):
    lo = 0
    hi = len(nums) - 1
    ans = 0
    while (lo <= hi):
        mi = (lo + hi) // 2
        if (nums[mi] < target):
            lo = mi + 1
            ans = mi + 1
        elif (nums[mi] > target):
            hi = mi - 1
        else:
            ans = mi
            return ans
    return ans
        
nums = [1,3,5,6] 
target = 2
print(searchInsert(nums, target))