# https://leetcode.com/problems/find-k-closest-elements/description/

def findClosestElements(arr, k, x):
    n = len(arr)
    left = 0
    right = n - 1
    while right - left >= k:
        if abs(arr[left] - x) <= abs(arr[right] - x):
            right -= 1
        else:
            left += 1

    return arr[left:left+k]




arr1 = [1,2,3,4,5]
k1 = 4
x1 = 3
arr2 = [1,1,2,3,4,5]
k2 = 4
x2 = -1
arr3 = [1,1,1,10,10,10]
k3 = 1
x3 = 9
arr4 = [1]
k4 = 1
x4 = 1
arr5 = [0,0,0,1,3,5,6,7,8,8]
k5 = 2
x5 = 2
print(findClosestElements(arr1, k1, x1))