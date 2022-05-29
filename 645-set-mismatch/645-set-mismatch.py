class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            arr[nums[i]] += 1
        ans = [-1, -1]
        for i in range(1, len(nums) + 1):
            if arr[i] == 2:
                ans[0] = i
            if arr[i] == 0:
                ans[1] = i
        return ans