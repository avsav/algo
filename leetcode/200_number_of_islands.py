# https://leetcode.com/problems/number-of-islands/description/

def numIslands(grid):
    row = len(grid)
    col = len(grid[0])
    cnt = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == "1":
                dfs(grid, r, c)
                cnt += 1
    return cnt

def dfs(grid, r, c):
    row = len(grid)
    col = len(grid[0])
    dirX = [1,0,-1,0]
    dirY = [0,1,0,-1]

    grid[r][c] = "0"
    for i in range(4):
        nextRow = r + dirX[i]
        nextCol = c + dirY[i]
        if 0 <= nextRow < row and 0 <= nextCol < col and grid[nextRow][nextCol] == "1":
            dfs(grid, nextRow, nextCol)




grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid2))