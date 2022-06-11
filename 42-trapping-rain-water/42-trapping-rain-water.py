class Solution:
    def trap(self, height):
        stack, res = [], 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                bottom = stack.pop(-1)
                res += 0 if not stack else ((
                    min(height[i], height[stack[-1]])-height[bottom])*(i - stack[-1] - 1))
            stack.append(i)
        return res