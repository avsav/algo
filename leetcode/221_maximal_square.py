# https://leetcode.com/problems/maximal-square

def maximalSquare(matrix):
    m = len(matrix)
    n = len(matrix[0])
    maxLen = 0
    dp = [[0]*(n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            maxLen = max(maxLen, dp[i][j])

    return maxLen * maxLen




matrix1 = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
matrix2 = [["0","1"],
           ["1","0"]]
matrix3 = [["0"]]
print(maximalSquare(matrix1))