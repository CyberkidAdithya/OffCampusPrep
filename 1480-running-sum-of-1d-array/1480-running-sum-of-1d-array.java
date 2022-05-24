class Solution {
    public int[] runningSum(int[] nums) {
        int summ = 0;
        int ans[] = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            summ += nums[i];
            ans[i] = summ;
        }
        return ans;
    }
}