# https://leetcode.com/problems/3sum/

def threeSum(nums):
    n = len(nums)
    res = []
    for i in range(n):
       two = twoSum(nums, -nums[i])
       for t in two:
            #if nums[i] not in t:
            t.append(nums[i])
            t.sort()
            if t not in res:
                res.append(t)
            
    return res


def twoSum(nums, target):
    n = len(nums)
    s = set()
    res = []
    for i in range(n):         
        complement = target - nums[i]
        if complement in s and [nums[i], complement] not in res:
            res.append([complement, nums[i]])
        s.add(nums[i])
    return res



nums1 = [1,-1,3,5]
nums2 = [-1,0,1,2,-1,-4]
nums3 = [0,1,1]
nums4 = [0,0,0]
print(twoSum(nums2, 0))
print(threeSum(nums2))