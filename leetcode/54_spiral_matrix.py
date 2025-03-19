# https://leetcode.com/problems/spiral-matrix/description/

def spiralOrder(matrix):
    n = len(matrix)
    m = len(matrix[0])
    left = 0
    right = m - 1
    up = 0
    down = n - 1
    res = []
    while left <= right and up <= down:
        for i in range(left, right + 1):
            res.append(matrix[up][i])
        up += 1
        for i in range(up, down + 1):
            res.append(matrix[i][right])
        right -= 1
        if up <= down:
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
        if left <= right:
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
    
    return res


matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix3 = [[1,2,3,4]]
matrix4 = [[1]]
print(spiralOrder(matrix3))