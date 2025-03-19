class Solution {
public:
    int minOperations(vector<int>& nums) {
        int count = 0;
        int n = nums.size();

        for (int i = 0; i < n; ++i) {
            if (nums[i] == 0) {
                // If we don't have enough elements to flip, return -1
                if (i + 2 >= n) return -1;

                // Flip the next three elements
                for (int j = i; j < i + 3; ++j) {
                    nums[j] = 1 - nums[j];  // Toggle between 0 and 1
                }
                
                count++;  // Increment operation count
            }
        }
        return count;
    }
};