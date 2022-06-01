import sys
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]    # make the grid
        
        dp[0][0] = 0 if grid[0][0] else 1
        for i in range(1, m):  # base condition: to reach 1st row, the robot SHOULD MOVE IN RIGHT ONLY
            dp[i][0] = 0 if grid[i][0] else dp[i - 1][0]

        for i in range(1, n):  # base conditon: to reach 1st col, the robot SHOULD MOVE IN DOWN ONLY
            dp[0][i] = 0 if grid[0][i] else dp[0][i - 1]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    temp = 0
                    if grid[i][j - 1] == 0:
                        temp += dp[i][j - 1]
                    if grid[i - 1][j] == 0:
                        temp += dp[i - 1][j]
                    dp[i][j] = temp     # the robot can reach FROM LEFT OR FROM ABOVE to any given cell
        print(*dp, sep = "\n")
        
        return dp[-1][-1]