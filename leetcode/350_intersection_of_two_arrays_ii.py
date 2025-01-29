# https://leetcode.com/problems/intersection-of-two-arrays-ii/

def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    
    n1 = len(nums1)
    n2 = len(nums2)
    len_ht1 = nums1[n1 - 1] + 1
    len_ht2 = nums2[n2 - 1] + 1
    ht1 = [0] * (len_ht1)
    ht2 = [0] * (len_ht2)

    for num in nums1:
        ht1[num] += 1
    
    for num in nums2:
        ht2[num] += 1

    res = []
    for i in range(min(len_ht1, len_ht2)):
        if ht1[i] > 0 and ht2[i] > 0:
            for k in range(min(ht1[i], ht2[i])):
                res.append(i)
    
    return res

        
nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2))