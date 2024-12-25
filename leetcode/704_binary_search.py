# https://leetcode.com/problems/binary-search/description/

def search(nums, target):
    low = 0
    high = len(nums) - 1

    while (low <= high):
        mi = (low + high) // 2
        if (nums[mi] > target):
            high = mi - 1
        elif (nums[mi] < target):
            low = mi + 1            
        else:
            return mi
    return -1
    
target = 2
nums = [-1,0,3,5,9,12]
print(search(nums, target))


