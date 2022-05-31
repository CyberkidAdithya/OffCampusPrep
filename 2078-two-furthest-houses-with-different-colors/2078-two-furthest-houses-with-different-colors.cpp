class Solution {
public:
    int maxDistance(vector<int>& colors) {
        int n = colors.size();
        int beg = 0, end = n - 1;
        while (colors[beg] == colors[n - 1]) {
            beg += 1;
        }
        int res1 = end - beg;
        beg = 0, end = n - 1;
        while (colors[beg] == colors[end]) {
            end -= 1;
        }
        int res2 = end - beg;
        return max(res1, res2);
        
    }
};