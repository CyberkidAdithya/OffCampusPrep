class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        px, py = -1, -1
        found = False
        for i in range(m):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    px, py = i, j
                    found = True
                    break
        peri = 0
        def fill(x, y):
            nonlocal peri
            if x < 0 or x >= m:
                peri += 1
                return
            if y < 0 or y >= n:
                peri += 1
                return
            if grid[x][y] == 0:
                peri += 1
                return
            if grid[x][y] == 2:
                return
            grid[x][y] = 2
            fill(x + 1, y)
            fill(x - 1, y)
            fill(x, y + 1)
            fill(x, y - 1)
        fill(px, py)
        return peri