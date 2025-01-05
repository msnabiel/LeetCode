class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        int n = s.size();
        vector<int> diff(n + 1, 0); // Difference array to track cumulative shifts

        // Process each shift operation
        for (int i = 0; i < shifts.size(); ++i) {
            int start = shifts[i][0];
            int end = shifts[i][1];
            int direction = shifts[i][2]; // 1 for forward, 0 for backward
            int delta = direction == 1 ? 1 : -1;

            // Update the difference array
            diff[start] += delta;
            diff[end + 1] -= delta;
        }

        // Apply the cumulative shifts to the string
        int cumulativeShift = 0;
        for (int j = 0; j < n; ++j) {
            cumulativeShift += diff[j]; // Compute the net shift at position j
            cumulativeShift = (cumulativeShift % 26 + 26) % 26; // Normalize within [0, 25]

            // Apply the normalized shift to the character
            s[j] = (s[j] - 'a' + cumulativeShift) % 26 + 'a';
        }

        return s;
    }
};