class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def check(x, y):
            if x < 0 or x >= m:
                return 0
            if y < 0 or y >= n:
                return 0
            if grid[x][y] == "0":
                return 0
            return 1
        def fill(x, y):
            if check(x, y):
                grid[x][y] = "0"
                fill(x + 1, y)
                fill(x - 1, y) 
                fill(x, y + 1) 
                fill(x, y - 1)
            return
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    fill(i, j)
        return ans