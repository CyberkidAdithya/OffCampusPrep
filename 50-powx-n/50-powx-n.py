class Solution:
    def myPow(self, x: float, n: int) -> float:
        def findpow_iter(a, b, m = int(1e9 + 7)):    #iterative
            if a == 0:
                return 0
            res = 1 
            while b > 0:
                if b & 1:
                    res = res * a
                a = a * a
                b >>= 1
            return res
        return findpow_iter(x, n) if n >= 0 else pow(x, n)