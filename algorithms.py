from random import randrange


#### Randomized quick sort ####
# Cormen
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


#### Merge sort ####
def merge(a, b):
    c = []
    while a or b:
        if not b or (a and a[0] < b[0]):
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    return c

def mergesort(arr):
    m = len(arr) // 2
    if m == 0:
        return arr
    return merge(mergesort(arr[:m]), mergesort(arr[m:]))


#### Binary search ####
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mi = (low + high) // 2
        if nums[mi] > target:
            high = mi - 1
        elif nums[mi] < target:
            low = mi + 1            
        else:
            return mi     
    return -1
 


arr0 = [2, 8, 7, 1, 3, 5, 6, 4]
arr1 = [1, 2, 7, 3, 4, 0, -1, 3, 8, 10, 12, 1, 6, 4, -10, 20]
arr2 = [1, 1, 1, 1, 1]
arr3 = [5, 4, 3, 2, 1, 0]
arr4 = [3]
#partition(arr0, 0, len(arr0) - 1)
quicksort(arr0, 0, len(arr0) - 1)
print(arr0)
print(mergesort(arr0))


#nums = [2, 8, 9, 10, 13, 14]
#print(binary_search(nums, 12))

#a = [1, 5, 7]
#b = [2, 4]
#print(merge(a, b))
#print(a[2:])