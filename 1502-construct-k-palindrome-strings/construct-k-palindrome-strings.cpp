class Solution {
public:
    bool canConstruct(string s, int k) {
        int n = s.size();
        if (n < k) return false;

        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        int oddCount = 0;
        for (auto& entry : freq) {
            if (entry.second % 2 != 0) {
                oddCount++;
            }
        }

        return oddCount <= k;
    }
};