class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        def check(x, y):
            if x < 0 or x >= m:
                return 0
            if y < 0 or y >= n:
                return 0
            if grid2[x][y] == 0:
                return 0
            return 1
        def fill(x, y):
            if check(x, y) == 0:
                return 1
            if grid2[x][y] == 1 and grid1[x][y] == 0:
                return 0
            grid2[x][y] = 0
            res = fill(x + 1, y) & fill(x - 1, y) & fill(x, y + 1) & fill(x, y - 1)
            return res
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 1 and grid2[i][j] == 1:
                    ans += fill(i, j) > 0
        return ans