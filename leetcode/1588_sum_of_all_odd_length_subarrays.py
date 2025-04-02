# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/


def sumOddLengthSubarrays(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        res += ((i + 1) * (n - i) + 1)//2 * arr[i]

    return res


arr1 = [1,4,2,5,3]
arr2 = [1,2]
arr3 = [10,11,12]
print(sumOddLengthSubarrays(arr3))