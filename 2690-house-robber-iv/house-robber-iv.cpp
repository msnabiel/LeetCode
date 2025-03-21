class Solution {
public:
    bool canRob(vector<int>& nums, int k, int maxCap) {
        int count = 0; // Number of houses robbed
        int n = nums.size();
        
        for (int i = 0; i < n; i++) {
            if (nums[i] <= maxCap) { 
                count++; // Rob this house
                i++; // Skip next house (constraint: can't rob adjacent houses)
            }
            if (count >= k) return true; // If we've robbed k houses, return true
        }
        return false;
    }

    int minCapability(vector<int>& nums, int k) {
        int left = *min_element(nums.begin(), nums.end()); // Min possible money
        int right = *max_element(nums.begin(), nums.end()); // Max possible money
        int result = right;

        while (left <= right) {
            int mid = left + (right - left) / 2; // Middle value as potential max capability
            if (canRob(nums, k, mid)) {
                result = mid; // Try to find a smaller max capability
                right = mid - 1;
            } else {
                left = mid + 1; // Increase capability to make it possible
            }
        }
        return result;
    }
};