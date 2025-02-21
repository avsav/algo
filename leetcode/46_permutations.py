# https://leetcode.com/problems/permutations/

def permute(nums):
    nums.sort()
    res = [nums[:]]
    next_nums = nums
    while next_nums != nums[::-1]:
        next_nums = next_permutation(next_nums[:])
        res.append(next_nums)
    return res

def next_permutation(nums):
    n = len(nums)
    k = n - 2
    while nums[k] > nums[k + 1]:
        k -= 1
    t = k + 1
    while t < n - 1 and nums[t + 1] > nums[k]:
        t += 1
    if k < 0:
        return nums
    nums[k], nums[t] = nums[t], nums[k]
    rev(nums, k + 1, n - 1)
    return nums
    """
    a = nums[:k+1]
    b = nums[k+1:][::-1]
    a.extend(b)
    return a
    """

def rev(nums, start, end):
    left = start
    right = end #len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1



nums1 = [1, 3, 5, 4, 2]
nums2 = [1, 2, 3, 4]
nums3 = [3, 2, 1]
nums4 = [0, 1]
nums5 = [1, 3, 2] 
print(next_permutation(nums5))
rev(nums1, 0, 4)
print(nums1)
#print(permute(nums2))



