class Solution {
public:
    int minCapability(vector<int>& nums, int k) {
        int left = nums[0], right = nums[0];
        int n = nums.size();
        for (int i = 1; i < n; i++) {
            if (nums[i] > right) right = nums[i];
            if (nums[i] < left) left = nums[i];
        }
        while (left <= right) {
            int mid = (left + right) / 2;
            if (check(nums, mid, k)) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }
private:
    bool check(vector<int>& nums, int guess, int k) {
        int n = nums.size();
        if (n == 1) return nums[0] <= guess;
        int count = 0; 
        for (int i = 0; i < n; i++) {
            if (nums[i] <= guess) {
                count++;
                i++;
            }
        }
        if (count >= k) return true;
        return false;
    }
};