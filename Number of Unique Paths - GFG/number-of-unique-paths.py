#User function Template for python3

   
class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        #code here
        m, n = a, b
        dp = [[0] * n for _ in range(m)]    # make the grid
        
        for i in range(m):  # base condition: to reach 1st row, the robot SHOULD MOVE IN RIGHT ONLY
            dp[i][0] = 1

        for i in range(n):  # base conditon: to reach 1st col, the robot SHOULD MOVE IN DOWN ONLY
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]  # the robot can reach FROM LEFT OR FROM ABOVE to any given cell
                
        return dp[-1][-1]   # return the bottom corner cell
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a_b = [int(x) for x in input().strip().split()]
        a = a_b[0]
        b = a_b[1]
        ob = Solution()
        print(ob.NumberOfPaths(a, b))

# } Driver Code Ends