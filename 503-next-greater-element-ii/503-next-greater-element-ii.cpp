class Solution {
public:
    
    vector<int> monotonicStack(vector<int> arr, int n) {
        stack<int> stack;
        vector<int> nge(n, -1);
        for (int i = 2 * n - 1; i > -1; i--) {
            while ((stack.size() != 0) and (arr[i % n] >= stack.top())) {
                stack.pop();
            }
            if (stack.size() != 0) {
                nge[i % n] = stack.top();
            }
            stack.push(arr[i % n]);
        }
        return nge;
    }
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> greater = monotonicStack(nums, nums.size());
        return greater;
    }
};
