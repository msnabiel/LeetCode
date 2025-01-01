class Solution {
public:
    int maxScore(string s) {
        int totalOnes = 0;
        for (char c : s) {
            if (c == '1') totalOnes++;
        }
        
        int zerosSoFar = 0;
        int onesSoFar = 0;
        int maxScore = 0;
        
        // Iterate through all possible splits
        for (int i = 0; i < s.size() - 1; i++) {
            if (s[i] == '0') zerosSoFar++;
            else onesSoFar++;
            
            // Calculate score for the current split
            int score = zerosSoFar + (totalOnes - onesSoFar);
            maxScore = max(maxScore, score);
        }
        
        return maxScore;
    }
};