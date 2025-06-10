# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

def findDifference(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    res1 = []
    res2 = []
    for num in nums1:
        if num not in nums2:
            res1.append(num)

    for num in nums2:
        if num not in nums1:
            res2.append(num)

    return [res1, res2]

nums1_1 = [1,2,3]
nums2_1 = [2,4,6]
nums1_2 = [1,2,3,3]
nums2_2 = [1,1,2,2]

print(findDifference(nums1_2, nums2_2))