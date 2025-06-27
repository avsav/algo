# https://leetcode.com/problems/3sum/

def threeSum(nums):
    nums.sort()
    n = len(nums)
    s = set()
    for i in range(n):
        j = i + 1
        k = n - 1
        while j < k:
            total = nums[j] + nums[k]
            if total == -nums[i]:
                triplet = (nums[i], nums[j], nums[k])
                # if triplet not in res:
                s.add(triplet)
                j += 1
                k -= 1
            elif total < -nums[i]:
                j += 1
            else:
                k -= 1

    res = []
    for triplet in s:
        res.append(list(triplet))
    return res



nums1 = [1,-1,3,5]
nums2 = [-1,0,1,2,-1,-4]
nums3 = [0,1,1]
nums4 = [0,0,0]
nums5 = [-2,0,1,1,2]
nums6 = [0,0,0,0]
print(threeSum(nums2))