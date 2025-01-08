class Solution {
public:
    bool isPrefixAndSuffix(const string& str1, const string& str2) {
        int n = str1.size();
        int m = str2.size();
        if (n > m) return false; 
        
        if (str2.substr(0, n) != str1) return false;
        if (str2.substr(m - n, n) != str1) return false;
        
        return true;
    }
    
    int countPrefixSuffixPairs(vector<string>& words) {
        int count = 0;
        int n = words.size();
        
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                // Check if words[i] is both a prefix and suffix of words[j]
                if (isPrefixAndSuffix(words[i], words[j])) {
                    count++;
                }
            }
        }
        
        return count;
    }
};