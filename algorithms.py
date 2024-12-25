from random import randrange


#### Quicksort ####
def partition(arr, p, r):
    k = randrange(p, r + 1)
    arr[k], arr[r] = arr[r], arr[k]
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)


#### Binary search ####
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while (low <= high):
        mi = (low + high) // 2
        if (nums[mi] > target):
            high = mi - 1
        elif (nums[mi] < target):
            low = mi + 1            
        else:
            return mi     
    return -1
 

 
arr0 = [2, 8, 7, 1, 3, 5, 6, 4]
arr1 = [1, 2, 7, 3, 4, 0, -1, 3, 8, 10, 12, 1, 6, 4, -10, 20]
arr2 = [1, 1, 1, 1, 1]
arr3 = [5, 4, 3, 2, 1, 0]
#partition(arr0, 0, len(arr0) - 1)
quicksort(arr0, 0, len(arr0) - 1)
print(arr0)
