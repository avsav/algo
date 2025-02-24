# https://leetcode.com/problems/set-matrix-zeroes/description/

def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    zc = zr = False
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if i == 0:
                    zr = True
                if j == 0:
                    zc = True
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if zr:
        for j in range(n):
            matrix[0][j] = 0
    if zc:
        for i in range(m):
            matrix[i][0] = 0

    return matrix

matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(matrix2))