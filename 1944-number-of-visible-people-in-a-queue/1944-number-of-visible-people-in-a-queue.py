class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        stack = []  # monotonic stack
        for i in range(n - 1, -1, -1):
            while stack and heights[i] > stack[-1]:
                stack.pop()
                ans[i] += 1 # smaller heights are popped until we encounter a bigger element
            if stack:
                ans[i] += 1 # rest of the stack elements to the right will be hidden by this element
            stack.append(heights[i])
        return ans