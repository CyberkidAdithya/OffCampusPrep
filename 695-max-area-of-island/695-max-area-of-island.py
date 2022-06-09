class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        globalmaxarea = 0
        def fill(x, y):
            nonlocal localmaxarea
            if x < 0 or x >= m:
                return 0
            if y < 0 or y >= n:
                return 0
            if grid[x][y] == 0:
                return 0
            if grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return 1 + fill(x + 1, y) + fill(x - 1, y) + fill(x, y + 1) + fill(x, y - 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    localmaxarea = fill(i, j)
                    globalmaxarea = max(globalmaxarea, localmaxarea)
        return globalmaxarea