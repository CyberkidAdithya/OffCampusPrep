class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        localmax = globalmax = nums[0]
        for i in range(1, len(nums)):
            localmax = max(nums[i], localmax + nums[i])
            if localmax > globalmax:
                globalmax = localmax
        localmin = globalmin = nums[0]
        for i in range(1, len(nums)):
            localmin = min(nums[i], localmin + nums[i])
            if localmin < globalmin:
                globalmin = localmin
        return max(globalmax, sum(nums) - globalmin) if globalmax > 0 else globalmax