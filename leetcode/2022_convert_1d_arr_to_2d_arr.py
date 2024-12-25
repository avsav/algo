# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/

def construct2DArray(original, m, n):
    li = []
    if len(original) != m * n:
        return []
    for k in range(1, m + 1):
        li.append([original[i] for i in range((k - 1)*n, k*n)])
    return li


original = [1,2]
m = 1
n = 1
print(construct2DArray(original, m, n))