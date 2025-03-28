# https://leetcode.com/problems/duplicate-zeros/description/


def duplicateZeros(arr):
    n = len(arr)
    last = 0
    cnt = 0
    flag = False
    for i in range(n):
        if arr[i] == 0:
            cnt += 2
        else:
            cnt += 1
        if cnt == n:
            last = i
            break
        if cnt - n == 1:
            flag = True
            last = i
            break

    i = n - 1
    while i >= 0:
        arr[i] = arr[last]
        if arr[last] == 0 and not flag:
            i -= 1
            arr[i] = 0
        i -= 1
        last -= 1
        flag = False

    return arr

    


arr1 = [1,0,2,3,0,4,5,0]
arr2 = [1,2,3]
arr3 = [8,4,5,0,0,0,0,7]
print(duplicateZeros(arr2))
