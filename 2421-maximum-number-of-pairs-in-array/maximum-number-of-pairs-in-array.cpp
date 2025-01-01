#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> numberOfPairs(vector<int>& nums) {
        unordered_map<int, int> freq_map; 
        int pairs = 0;
        int leftovers = 0;
        
        // Count the frequency of each number
        for (int num : nums) {
            freq_map[num]++;
        }
        
        // Calculate pairs and leftovers
        for (const auto& entry : freq_map) {
            pairs += entry.second / 2; // Each pair consists of two numbers
            leftovers += entry.second % 2; // Any leftover number is a single integer
        }
        
        // Return the result as a vector of two integers: number of pairs and leftovers
        return {pairs, leftovers};
    }
};