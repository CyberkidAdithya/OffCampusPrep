class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        cnt = i = 0
        while i < len(s):
            while stack and stack[-1] != s[i]:
                stack.pop()
                i += 1
            if i > 0 and len(stack) == 0:
                cnt += 1
            if i < len(s):
                stack.append(s[i])
            i += 1
        return cnt