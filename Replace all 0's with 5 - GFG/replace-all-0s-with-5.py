#function should return an integer
#your task is to compplete this function
class Solution:
    def convertFive(self,n):
        #Code here
        x = 0
        num = n
        while num:
            y = num % 10
            x = x * 10 + (y if y != 0 else 5)
            num //= 10
        num = x
        x = 0
        while num:
            y = num % 10
            x = x * 10 + y
            num //= 10
        return x
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        print(Solution().convertFive(n))
# Contributed by: Harshit sidhwa

# } Driver Code Ends