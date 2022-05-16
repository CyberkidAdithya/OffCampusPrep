class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for x in jewels:
            ans += stones.count(x)
        return ans
            