class Solution(object):
    def minPathSum(self, arr):
        m, n = len(arr), len(arr[0])
        dis = [[0 for c in range(n)] for r in range(m)]
        dis[0][0] = arr[0][0]
        for i in range(1, m):   #going down first col
            dis[i][0] = dis[i - 1][0] + arr[i][0]
        for i in range(1, n):   #going right first row
            dis[0][i] = dis[0][i - 1] + arr[0][i]
        for i in range(1, m):
            for j in range(1, n):
                # check moving right or coming down is cheap to reach each cell
                dis[i][j] = arr[i][j] + min(dis[i - 1][j], dis[i][j - 1])
        return dis[-1][-1]