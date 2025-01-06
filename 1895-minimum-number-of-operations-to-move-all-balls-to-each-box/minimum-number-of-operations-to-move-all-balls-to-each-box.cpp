class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();
        vector<int> ans(n, 0);
        for(int i = 0; i < n; ++i) {
            int sum = 0;
            for(int j = 0; j < n; ++j) {
                if(i != j && boxes[j] == '1') {
                    int diff = abs(i - j);
                    sum += diff;
                }
            }
            ans[i] = sum;
        }
        return ans;
    }
};