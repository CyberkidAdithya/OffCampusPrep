class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        vector<int> ans(arr.size(), -1);
        int maxx = -1;
        for (int i = arr.size() - 1; i > 0; i--) {
            maxx = max(maxx, arr[i]);    
            ans[i - 1] = maxx;
        }
        return ans;   
    }
};