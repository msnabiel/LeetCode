class Solution {
public:
    long long findScore(vector<int>& nums) {
        int n = nums.size();
        vector<bool> marked(n, false);
        vector<int> indices(n);
        
        // Populate the indices array
        for (int i = 0; i < n; ++i) {
            indices[i] = i;
        }
        
        // Sort indices by the values in nums, then by index
        sort(indices.begin(), indices.end(), [&](int a, int b) {
            return nums[a] < nums[b] || (nums[a] == nums[b] && a < b);
        });
        
        long long score = 0;
        
        // Process each index in sorted order
        for (int idx : indices) {
            if (!marked[idx]) {
                // Add to score
                score += nums[idx];
                
                // Mark the current index and adjacent indices
                marked[idx] = true;
                if (idx > 0) marked[idx - 1] = true;
                if (idx < n - 1) marked[idx + 1] = true;
            }
        }
        
        return score;
    }
};