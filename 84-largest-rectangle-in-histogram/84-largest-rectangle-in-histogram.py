class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        pstack, hstack = [], []
        currarea, maxarea = 0, 0
        heights.append(0)
        for i in range(len(heights)):
            prevwidth = int(1e9)
            while hstack != [] and hstack[-1] > heights[i]:
                prevwidth = pstack[-1]
                width = i - pstack.pop()
                height = hstack.pop()
                currarea = width * height
                maxarea = max(currarea, maxarea)
            if hstack == [] or hstack[-1] < heights[i]:
                hstack.append(heights[i])
                pstack.append(min(prevwidth, i))
        return maxarea