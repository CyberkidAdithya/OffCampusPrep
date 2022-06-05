class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        stack = []
        for i in range(len(nums)):
            if not stack:
                stack.append(nums[i])
            else:
                if stack[-1] == nums[i]:
                    continue
                else:
                    stack.append(nums[i])
        flag = True
        for i in range(1, len(stack) - 1):
            if stack[i - 1] < stack[i] > stack[i + 1]:
                flag = False
                break
            elif stack[i - 1] > stack[i] < stack[i + 1]:
                flag = False
                break
        return flag
                
                    