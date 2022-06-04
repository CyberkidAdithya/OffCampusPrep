class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        # self.ans = 0
        m = len(grid)
        n = len(grid[0])
        # islandcount = 0
        
        def isvalid(x, y):
            return (0 <= x < m and 0 <= y < n)

        def dfs(x, y):
            if not isvalid(x, y):
                return
            if grid[x][y] == "X" or grid[x][y] == "Y": # if ending square
                return
            grid[x][y] = "Y" # mark visited
            dfs(x - 1, y)    # left
            dfs(x + 1, y)    # right
            dfs(x, y - 1)    # up
            dfs(x, y + 1)    # down
            return
    
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    if grid[i][j] == "O":
                        dfs(i, j)
                        # islandcount += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "O":
                    grid[i][j] = "X"
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "Y":
                    grid[i][j] = "O"

        # return self.ans
        # return islandcount
        