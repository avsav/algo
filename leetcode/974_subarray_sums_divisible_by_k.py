# https://leetcode.com/problems/subarray-sums-divisible-by-k/

def subarraysDivByK(nums, k):
    n = len(nums)
    prefix = res = 0
    divByK = notDivByK = 0
    for num in nums:
        prefix += num
        if prefix % k:
            notDivByK += 1
            res += divByK + 1
        else:
            divByK += 1
            res += notDivByK 


    return res


k1 = 2
nums1 = [1,3]
k2 = 5
nums2 = [4,5,0,-2,-3,1]
k3 = 9
nums3 = [5]
print(subarraysDivByK(nums1, k1))