# https://leetcode.com/problems/count-elements-with-maximum-frequency/

from collections import defaultdict

def maxFrequencyElements(nums):
    d = defaultdict(int)
    for num in nums:
        d[num] += 1
    max = 0
    for key, val in d.items():
        if val > max:
            max = val
    cnt = 0
    for key, val in d.items():
        if val == max:
            cnt += max
    return cnt

nums = [1,2,2,3,1,4]
print(maxFrequencyElements(nums))