class Solution {
public:
    int lengthAfterTransformations(string s, int t) {
        const int MOD = 1e9 + 7;
        vector<long long> freq(26, 0);

        for (char c : s)
            freq[c - 'a']++;

        while (t--) {
            vector<long long> nextFreq(26, 0);
            for (int i = 0; i < 26; ++i) {
                if (i == 25) {
                    nextFreq[0] = (nextFreq[0] + freq[25]) % MOD; // 'a'
                    nextFreq[1] = (nextFreq[1] + freq[25]) % MOD; // 'b'
                } else {
                    nextFreq[i + 1] = (nextFreq[i + 1] + freq[i]) % MOD;
                }
            }
            freq = nextFreq;
        }

        long long result = 0;
        for (int i = 0; i < 26; ++i)
            result = (result + freq[i]) % MOD;

        return result;
    }
};
