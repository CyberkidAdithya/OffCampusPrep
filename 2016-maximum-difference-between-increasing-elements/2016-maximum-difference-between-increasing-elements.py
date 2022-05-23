class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxx, minn = -1, nums[0]
        for i in range(len(nums)):
            maxx = max(maxx, nums[i] - minn)
            minn = min(minn, nums[i])
        return maxx if maxx != 0 else -1