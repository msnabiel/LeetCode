class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        for (int i = n - 1; i >= 0; --i) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0; // Reset current digit to 0 if it becomes 10
        }
        // If all digits were 9, we need to add a new leading 1
        digits.insert(digits.begin(), 1);
        return digits;
    }
};