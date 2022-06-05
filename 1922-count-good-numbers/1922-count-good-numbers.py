class Solution:
    def findpow_iter(self, a, b, m = int(1e9 + 7)):    #iterative
        if a == 0:
            return 0
        res = 1 
        while b > 0:
            if b & 1:
                res = res * a % m
            a = a * a % m
            b >>= 1
        return res % m
    def countGoodNumbers(self, n: int) -> int:
        odd = n // 2
        eve = n - odd
        mod = int(1e9 + 7)
        ans = self.findpow_iter(5, eve, mod) * self.findpow_iter(4, odd, mod)
        return ans % mod