class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]    # make the grid
        
        for i in range(m):  # base condition: to reach 1st row, the robot SHOULD MOVE IN RIGHT ONLY
            dp[i][0] = 1

        for i in range(n):  # base conditon: to reach 1st col, the robot SHOULD MOVE IN DOWN ONLY
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]  # the robot can reach FROM LEFT OR FROM ABOVE to any given cell
                
        return dp[-1][-1]   # return the bottom corner cell