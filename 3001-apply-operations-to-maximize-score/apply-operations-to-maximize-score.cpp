#include <vector>
#include <unordered_set>
#include <stack>
#include <algorithm>

using namespace std;

const int MOD = 1e9 + 7;

class Solution {
public:
    // Function to count unique prime factors of a number
    int primeFactors(int n) {
        unordered_set<int> factors;
        for (int i = 2; i * i <= n; i++) {
            while (n % i == 0) {
                factors.insert(i);
                n /= i;
            }
        }
        if (n > 1) {
            factors.insert(n);
        }
        return factors.size();
    }

    int maximumScore(vector<int>& nums, int k) {
        int n = nums.size();
        vector<tuple<int, int, int>> arr; // {index, prime factors count, value}

        // Step 1: Compute prime factors count for each number
        for (int i = 0; i < n; i++) {
            arr.emplace_back(i, primeFactors(nums[i]), nums[i]);
        }

        // Step 2: Compute left limits using monotonic stack
        vector<int> left(n, -1), right(n, n);
        stack<pair<int, int>> stk;

        for (const auto& [i, f, x] : arr) {
            while (!stk.empty() && stk.top().first < f) {
                stk.pop();
            }
            if (!stk.empty()) {
                left[i] = stk.top().second;
            }
            stk.emplace(f, i);
        }

        // Step 3: Compute right limits
        while (!stk.empty()) stk.pop();

        for (int j = n - 1; j >= 0; j--) {
            int i = get<0>(arr[j]), f = get<1>(arr[j]);
            while (!stk.empty() && stk.top().first <= f) {
                stk.pop();
            }
            if (!stk.empty()) {
                right[i] = stk.top().second;
            }
            stk.emplace(f, i);
        }

        // Step 4: Sort in decreasing order of values
        sort(arr.begin(), arr.end(), [](const auto& a, const auto& b) {
            return get<2>(a) > get<2>(b);
        });

        // Step 5: Compute the maximum score
        long long ans = 1;
        for (const auto& [i, f, x] : arr) {
            long long l = left[i], r = right[i];
            long long count = (i - l) * (r - i); // Number of subarrays this element contributes to
            
            if (count <= k) {
                ans = ans * powMod(x, count, MOD) % MOD;
                k -= count;
            } else {
                ans = ans * powMod(x, k, MOD) % MOD;
                break;
            }
        }

        return ans;
    }

private:
    // Function to compute (base^exp) % mod using fast exponentiation
    long long powMod(long long base, long long exp, int mod) {
        long long result = 1;
        while (exp > 0) {
            if (exp % 2 == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp /= 2;
        }
        return result;
    }
};
