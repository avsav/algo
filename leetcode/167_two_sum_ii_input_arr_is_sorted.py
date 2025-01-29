# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        for right in range(1, len(numbers)):
            diff = target - numbers[left]
            num = self.binarySearch(numbers[right:], diff)
            if num == -1:
                left += 1
            else:
                return [left + 1, right + 1]
            
    
        def binarySearch(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mi = (low + high) // 2
            if nums[mi] > target:
                high = mi - 1
            elif nums[mi] < target:
                low = nums[mi] + 1
            else:
                return mi
        return -1
    

