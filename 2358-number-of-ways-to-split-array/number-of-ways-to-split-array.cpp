class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        long long total = 0; 
        for (int num : nums) {
            total += num;
        }
        
        long long sumleft = 0;
        int cnt = 0;
        int n = nums.size();
        
        for (int i = 0; i < n - 1; ++i) { 
            sumleft += nums[i];
            long long sumright = total - sumleft;
            if (sumleft >= sumright) {
                cnt++;
            }
        }
        
        return cnt;
    }
};