class Solution:
    def monotonicstack(self, arr, n):
        stack = []  # monotonic stack
        nge = [0] * n
        for i in range(2 * n - 1, -1, -1):
            while stack != [] and arr[i % n] >= arr[stack[-1]]:
                stack.pop()
            if stack == []:
                nge[i % n] = -1
            else:
                nge[i % n] = stack[-1]
            stack.append(i % n)
        return nge
    
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        greater = self.monotonicstack(nums, len(nums))
        ans = [nums[greater[i]] if greater[i] != -1 else -1 for i in range(len(nums))]
        return ans
