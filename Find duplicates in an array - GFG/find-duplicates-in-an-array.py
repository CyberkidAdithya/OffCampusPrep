import collections
class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	ans = []
    	hp = collections.defaultdict(lambda:0)
    	for i in range(n):
            hp[arr[i]] += 1
            if hp[arr[i]] > 1:
    	       if hp[arr[i]] == 2: ans.append(arr[i])
        return sorted(ans) if ans else [-1]
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends