class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        greedy = sorted(costs, reverse = True)
        ans = 0
        while greedy and coins >= greedy[-1]:
            coins -= greedy.pop()
            ans += 1
        return ans