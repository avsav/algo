# https://leetcode.com/problems/permutations/

def permute(nums):
    res = [nums]
    res.append(next_permutation(nums))
    if nums == nums[::-1]:
        return
    return permute(nums)

def next_permutation(nums):
    n = len(nums)
    k = n - 2
    while nums[k] > nums[k + 1]:
        k -= 1
    t = k + 1
    while t < n - 1 and nums[t + 1] > nums[k]:
        t += 1
    nums[k], nums[t] = nums[t], nums[k]
    if k >= 0:
        for i in range(k + 1, n//2):
            nums[i] = nums[n - k - i]
    return nums

nums1 = [1, 3, 5, 4, 2]
nums2 = [1, 2, 3]
nums3 = [3, 2, 1]
print(next_permutation(nums3))
#print(permute(nums2))
    


