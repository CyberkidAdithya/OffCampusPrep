#User function Template for python3

class Solution:
    def solve(self, arr, n):
        # code here
        arr.sort()
        num1, num2 = "", ""
        flg = True
        for i in range(n):
            if flg:
                num1 += str(arr[i])
            else:
                num2 += str(arr[i])
            flg = not flg
        num1 = int(num1) if num1 else 0
        num2 = int(num2) if num2 else 0
        return num1 + num2

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.solve(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends