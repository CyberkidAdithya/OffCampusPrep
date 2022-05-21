class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hp = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (hp.getOrDefault(target - nums[i], -1) != -1) {
                int[] ans = {i, hp.get(target - nums[i])};
                return ans;
            }
            hp.put(nums[i], i);
        }
        int[] ans = {-1, -1};
        return ans;
    }
}