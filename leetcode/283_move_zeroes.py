# https://leetcode.com/problems/move-zeroes/description/

def moveZeroes(nums):
    n = len(nums)

    # bad solution
    def sol1(nums):
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == 0: 
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
    

    # two-pointer approach 
    # Pseudocode:
    # [1]- Initialize a pointer 'left' to 0, and 'right' to the next element 1.
    # [2]- Iterate through the list using a 'right' pointer starting at 1 and 
    # moving to the right.
    # [3]- If the element at the 'left' pointer is non-zero, update 'left' to 'right' 
    # and continue to the next iteration.
    # [4]- If the element at the 'right' pointer is 0, continue to the next iteration 
    # without making any changes.
    # [5]- If the element at the 'right' pointer is non-zero, swap the elements at 
    # 'left' and 'right' to move the non-zero element to the 'left' position, 
    # then increment 'left'.
    # [6]- Continue this process for all elements in the list.
    # [7]- The function does not return anything but modifies the input list 
    # 'nums' in-place. 

    def sol2(nums):
        left = 0
        for right in range(1, n):
            if nums[left] != 0:
                left = right
                continue
            if nums[right] == 0:
                continue
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left] 
                left += 1
        return nums
    
    def sol3(nums):
        left = 0
        for right in range(1, n):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]     
            if nums[left] != 0:
                left += 1            
        return nums

    return sol3(nums)

nums = [0,0,1,0,3,12]
print(moveZeroes(nums))