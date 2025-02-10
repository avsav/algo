# https://leetcode.com/problems/product-of-array-except-self/description/

def productExceptSelf(nums):
    prod = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        prod[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        prod[i] *= suffix
        suffix *= nums[i]
    
    return prod

nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
