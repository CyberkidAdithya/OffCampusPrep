class Solution:
    def monotonicstack(self, arr, n):
        stack = []
        nge = arr[:]
        for i in range(n - 1, -1, -1):
            while stack and arr[i] < stack[-1]:
                stack.pop()
            if stack != []:
                nge[i] -= stack[-1]
            stack.append(arr[i])
        return nge
    def finalPrices(self, prices: List[int]) -> List[int]:
        greater = self.monotonicstack(prices, len(prices))
        return greater