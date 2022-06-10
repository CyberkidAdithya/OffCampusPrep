import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n= len(nums)
        hp = collections.defaultdict(lambda:0)
        ans = 0
        presum = [0,]
        for i in range(1, n + 1):
            presum.append(presum[-1] + nums[i - 1])
            if presum[i] == k:
                ans += 1
            if hp[presum[i] - k] > 0:
                ans += hp[presum[i] - k]
            hp[presum[i]] += 1
        return ans