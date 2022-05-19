#User function Template for python3

class Solution:
	def find_median(self, v):
		# Code here
		arr = sorted(v)
		if len(arr) % 2 == 0:
		    median = (arr[n // 2 - 1] + arr[n // 2]) // 2
		else:
		    median = arr[n // 2]
		return median

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends