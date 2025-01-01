class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // Sort greed factors and cookie sizes
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int i = 0; // Pointer for children
        int j = 0; // Pointer for cookies
        
        // Try to assign cookies to children
        while (i < g.size() && j < s.size()) {
            if (s[j] >= g[i]) {
                // The current cookie satisfies the child's greed
                i++; // Move to the next child
            }
            // Move to the next cookie
            j++;
        }
        
        // i represents the number of content children
        return i;
    }
};