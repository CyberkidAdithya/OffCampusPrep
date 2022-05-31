class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int globalmin = nums[0];
        int maxdiff = -1;
        for (int i = 0; i < nums.size(); i++) {
            maxdiff = max(maxdiff, nums[i] - globalmin);
            globalmin = min(globalmin, nums[i]);
        }
        if (maxdiff) {
           return maxdiff; 
        }
        return -1;
    }
};