class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx, minn = -1, prices[0]
        for i in range(len(prices)):
            maxx = max(maxx, prices[i] - minn)
            minn = min(minn, prices[i])
        return maxx