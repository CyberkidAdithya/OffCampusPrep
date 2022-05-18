class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxx = -1
        for i in range(1, len(nums)):
            for j in range(0, i):
                maxx = max(maxx, nums[i] - nums[j])
        return maxx if maxx else -1