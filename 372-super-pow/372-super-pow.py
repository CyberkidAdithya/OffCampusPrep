class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def findpow_iter(a, b, m = int(1e9 + 7)):    #iterative
            if a == 0:
                return 0
            res = 1 
            while b > 0:
                if b & 1:
                    res = res * a % m
                a = a * a % m
                b >>= 1
            return res % m
        return findpow_iter(a, int("".join([str(c) for c in b])), 1337)