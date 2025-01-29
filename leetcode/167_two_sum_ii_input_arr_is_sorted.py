# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers, target):
        left = 0
        for right in range(1, len(numbers)):
            diff = target - numbers[left]
            num = self.binarySearch(numbers, diff, right)
            if num == -1:
                left += 1
            else:
                return [left + 1, num + 1]
            
    
    def binarySearch(self, nums, target, left):
        low = left
        high = len(nums) - 1

        while low <= high:
            mi = (low + high) // 2
            if nums[mi] > target:
                high = mi - 1
            elif nums[mi] < target:
                low = mi + 1
            else:
                return mi
        return -1
    

obj = Solution()
nums = [2, 3, 4]
print(obj.twoSum(nums, 6))
