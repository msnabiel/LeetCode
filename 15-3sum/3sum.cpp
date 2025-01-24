class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::vector<std::vector<int>> result;
        int n = nums.size();
        
        // Sort the input array
        std::sort(nums.begin(), nums.end());
        
        for (int i = 0; i < n - 2; ++i) {
            // Skip duplicate elements to avoid repeating the same triplet
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int left = i + 1, right = n - 1;
            
            // Use two pointers to find the other two elements
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    // Skip duplicates for the left pointer
                    while (left < right && nums[left] == nums[left + 1]) ++left;
                    // Skip duplicates for the right pointer
                    while (left < right && nums[right] == nums[right - 1]) --right;
                    
                    // Move both pointers
                    ++left;
                    --right;
                } 
                else if (sum < 0) {
                    ++left; // Need a larger number
                } 
                else {
                    --right; // Need a smaller number
                }
            }
        }
        
        return result;
    }
};