class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0  
        hp = collections.defaultdict(lambda:0)
        hp2 = collections.defaultdict(lambda:1)
        for i in range(len(nums)):
            hp[nums[i]] += 1
            if hp[nums[i]] > 1:
                cnt += hp2[nums[i]]
                hp2[nums[i]] += 1
        return cnt
        