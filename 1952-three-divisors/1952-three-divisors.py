class Solution:
    def isThree(self, n: int) -> bool:
        def gcd_iter(a, b):
            while(b):
                a, b = b, a % b
            return a
        if n < 3:
            return False
        else:
            flag = False
            for i in range(2, n):
                if n % i == 0:
                    if i * i == n:
                        flag = True
                    else:
                        return False
            return flag