import java.lang.Math;
class Solution {
    public int maxProduct(int[] nums) {
        int globalMax = nums[0];
        int globalMin = nums[0];
        int localMax = nums[0];
        int localMin = nums[0];
        int ans = nums[0];
        for (int i = 1; i < nums.length; i++) {
            localMax = nums[i] * globalMax;
            localMin = nums[i] * globalMin;
            globalMax = Math.max(nums[i], Math.max(localMax, localMin));
            globalMin = Math.min(nums[i], Math.min(localMax, localMin));
            ans = Math.max(ans, globalMax);
        }
        return ans;
    }
}