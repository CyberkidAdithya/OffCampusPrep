class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        num = x
        while num > 0:
            las = num % 10
            rev = rev * 10 + las
            num //= 10
        return rev == x