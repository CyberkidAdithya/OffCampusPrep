class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd_iter(a, b):
            while(b):
                a, b = b, a % b
            return a
        small = min(nums)
        big = max(nums)
        return gcd(small, big)