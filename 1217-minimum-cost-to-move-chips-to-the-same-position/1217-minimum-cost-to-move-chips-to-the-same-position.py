class Solution:
    def minCostToMoveChips(self, arr: List[int]) -> int:
        odd = eve = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                eve += 1
            if arr[i] % 2 == 1:
                odd += 1
        return min(eve, odd)