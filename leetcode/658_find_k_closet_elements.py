# https://leetcode.com/problems/find-k-closest-elements/description/

def findClosestElements(arr, k, x):
    n = len(arr)
    #res = []
    minMod = 10**10
    for i in range(n):
        d = abs(x - arr[i])
        minMod = min(minMod, d)

    for i in range(n):
        if abs(x - arr[i]) == minMod:
            ind = i
            break


    if ind - k + 1 <= 0:
        left = 0
        right = k - 1
    else:
        left = ind - k + 1
        right = ind
    

    minSum = 10**10
    sumMod = 0
    i = 0
    while right + i < n:
        sumMod = sum(abs(x - arr[k]) for k in range(left + i, right + i + 1))
        minSum = min(minSum, sumMod)
        i += 1

    a = b = 0
    j = 0
    while right + j < n:
        sumMod = sum(abs(x - arr[k]) for k in range(left + j, right + j + 1))
        if sumMod == minSum:
            a = left + j
            b = right + j + 1
            break
        j += 1

    return arr[a:b]




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
print(findClosestElements(arr5, k5, x5))