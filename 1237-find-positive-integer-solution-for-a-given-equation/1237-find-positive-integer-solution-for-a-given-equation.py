"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        mx, my = -1, -1
        x, y = -1, -1
        ans = []
        for y in range(1, 1001):
            beg, end = 1, 1001
            found = False
            while beg <= end and not found:
                x = beg + (end - beg) // 2	# to avoid mid overflow
                n = customfunction.f(x, y)
                if n == z:				# condition
                    ans.append([x, y])
                    found = True
                    mx = x	 				# found index
                elif n < z:
                    beg = x + 1     
                else:
                    end = x - 1
        return ans