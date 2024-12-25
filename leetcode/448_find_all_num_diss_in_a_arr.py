# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

def findDisappearedNumbers(nums):
    n = len(nums)
    arr = (n + 1) * [0]
    for num in nums:
        arr[num] += 1

    items = []
    for i in range(1, n + 1):
      if (arr[i] < 1): items.append(i)

    return items
 
nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))
