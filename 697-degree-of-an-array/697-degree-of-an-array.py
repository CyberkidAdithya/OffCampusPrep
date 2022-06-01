import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hp = collections.defaultdict(lambda:0)
        maxfreq = ele = -1
        for i in range(len(nums)):
            hp[nums[i]] += 1
            if hp[nums[i]] > maxfreq:
                ele = nums[i]
                maxfreq = hp[nums[i]]
        elems = [x for x, y in hp.items() if y == maxfreq]
        ans = int(1e18)
        for ele in elems:
            i, j = 0, len(nums) - 1
            while nums[i] != ele:
                i += 1
            while nums[j] != ele:
                j -= 1
            ans = min(j - i + 1, ans)
        return ans