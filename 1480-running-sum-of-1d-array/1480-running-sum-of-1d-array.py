class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = list()
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            arr.append(summ)
        return arr