class Solution:
    def countHillValley(self, arr: List[int]) -> int:
        count = 0
        nums = []
        for i in range(len(arr)):
            if not nums:
                nums.append(arr[i])
            else:
                if nums[-1] == arr[i]:
                    continue
                else:
                    nums.append(arr[i])
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                count += 1
            if nums[i - 1] > nums[i] < nums[i + 1]:
                count += 1
        return count