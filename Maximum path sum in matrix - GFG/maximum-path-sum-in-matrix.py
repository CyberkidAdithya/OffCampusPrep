#User function Template for python3

import sys
class Solution:
    def maximumPath(self, n, matrix):
        row, col, result = n + 1, n + 1, -1e9
        dp = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                choices = [dp[i-1][j-1], dp[i-1][j]]
                if j+1 <= n:
                    choices.append(dp[i-1][j+1])
                dp[i][j] = matrix[i-1][j-1] + max(choices)
                result = max(result, dp[i][j])
        return result
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends