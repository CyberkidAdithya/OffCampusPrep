class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # self.ans = 0
        m = len(grid)
        n = len(grid[0])
        islandcount = 0
        
        def isvalid(x, y):
            return (0 <= x < m and 0 <= y < n)

        def dfs(x, y):
            if not isvalid(x, y):
                # print("DFS NOT CALL: ", x, y)
                return
            if grid[x][y] == "0": # if ending square
                # print("DFS NOT CALL: ", x, y)
                return
            # print("DFS CALL: ", x, y)
            grid[x][y] = "0" # mark visited
            dfs(x - 1, y)    # left
            dfs(x + 1, y)    # right
            dfs(x, y - 1)    # up
            dfs(x, y + 1)    # down
            return
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islandcount += 1
                
        # return self.ans
        return islandcount