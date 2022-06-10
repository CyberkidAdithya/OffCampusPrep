class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        hp = collections.defaultdict(lambda:0)
        prefixsum = 0
        for i in range(len(nums)):
            prefixsum += nums[i]
            if prefixsum % k == 0:
                ans += 1
            if hp[prefixsum % k] > 0:
                ans += hp[prefixsum % k]
            hp[prefixsum % k] += 1
        return ans