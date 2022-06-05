class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        summ = sum(nums)
        nums.sort(reverse = True)
        tot = 0
        ind = -1
        for i in range(len(nums)):
            tot += nums[i]
            ind = i
            if tot > summ - tot:
                break
        return nums[:ind + 1]