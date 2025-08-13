# https://leetcode.com/problems/subarray-product-less-than-k/description

def numSubarrayProductLessThanK(nums, k):
    n = len(nums)
    left = 0
    cnt = 0
    product = 1
    if k <= 0:
        return 0
    for right in range(n):
        product *= nums[right]
        while product >= k and left <= right:
            product /= nums[left]
            left += 1
        cnt += right - left + 1

    return cnt



nums1 = [10,5,2,6]
nums2 = [10,5,2]
k1 = 100
nums3 = [1,2,3]
k3= 0
nums4 = [1,1,1]
k4 = 1
print(numSubarrayProductLessThanK(nums1, k1))