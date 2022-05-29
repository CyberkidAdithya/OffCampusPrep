import collections
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hp = collections.defaultdict(lambda:0)
        for i in range(len(nums)):
            hp[nums[i]] += 1
            if hp[nums[i]] > 1:
                return nums[i]
