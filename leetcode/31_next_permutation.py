# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = n - 2
        while nums[k] > nums[k + 1]:
            k -= 1
        t = k + 1
        while t < n - 1 and nums[t + 1] > nums[k]:
            t += 1
        if k < 0:
            return nums[::-1]
        nums[k], nums[t] = nums[t], nums[k]
        self.rev(nums, k + 1, n - 1)
        return nums

    def rev(self, nums, start, end):
        left = start
        right = end 
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


nums1 = [1,2,3]
nums2 = [3,2,1]
nums3 = [1,1,5]
#print(nextPermutation(nums1))
print(nums2)
obj = Solution()
print(obj.nextPermutation(nums2))
#print(nextPermutation(nums3))