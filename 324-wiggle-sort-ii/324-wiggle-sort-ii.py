class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse = True)
        ans = [-1] * len(nums)
        ptr = 0
        for i in range(1, len(nums), 2):
            ans[i] = nums[ptr]
            ptr += 1
        for i in range(0, len(nums), 2):
            ans[i] = nums[ptr]
            ptr += 1
        for i in range(len(nums)):
            nums[i] = ans[i]