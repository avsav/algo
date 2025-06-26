# https://leetcode.com/problems/3sum/

def threeSum(nums):
    n = len(nums)
    indexes = []
    res = []
    for i in range(n):
       two_ind = twoSum(nums, -nums[i])
       for ind in two_ind:
            if i not in ind:
                ind.append(i)
                ind.sort()
                if ind not in indexes:
                    indexes.append(ind)

    for ind in indexes:
        triplet = []
        for i in ind:
            triplet.append(nums[i])
            triplet.sort()
        if triplet not in res:
            res.append(triplet)    
    return res


def twoSum(nums, target):
    n = len(nums)
    s = set()
    res = []
    for i in range(n):         
        complement = target - nums[i]
        if complement in nums:
            j = nums.index(complement)
        if complement in s:
            res.append([j, i])
        s.add(nums[i])
    return res





nums1 = [1,-1,3,5]
nums2 = [-1,0,1,2,-1,-4]
nums3 = [0,1,1]
nums4 = [0,0,0]
print(threeSum(nums4))
#print(twoSum(nums2, 0))