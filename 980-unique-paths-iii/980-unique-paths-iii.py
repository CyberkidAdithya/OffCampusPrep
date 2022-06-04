class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        m = len(grid)
        n = len(grid[0])
        notvisited = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j # starting square found
                elif grid[i][j] == 0:
                    notvisited += 1 # empty square found
        
        def isvalid(x, y):
            return (0 <= x < m and 0 <= y < n and grid[x][y] >= 0)
        
        def dfs(x, y, notvisited):
            if not isvalid(x, y):
                return
            if grid[x][y] == 2: # if ending square
                if notvisited == 0:
                    self.ans += 1
                return
            grid[x][y] = -2 # mark visited
            dfs(x - 1, y, notvisited - 1)    # left
            dfs(x + 1, y, notvisited - 1)    # right
            dfs(x, y - 1, notvisited - 1)    # up
            dfs(x, y + 1, notvisited - 1)    # down
            grid[x][y] = 0  # unmark visited
    
        dfs(x, y, notvisited)
        return self.ans
