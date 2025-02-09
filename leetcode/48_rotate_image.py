# https://leetcode.com/problems/rotate-image/description/

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j] 
    return matrix


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix))