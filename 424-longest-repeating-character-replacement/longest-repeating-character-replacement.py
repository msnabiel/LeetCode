from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        maxcount = 0
        freq = defaultdict(int)
        left = 0
        max_freq = 0  # max frequency of any char in current window

        for right in range(len(s)):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])

            # If flips needed exceed k, shrink window from left
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            maxcount = max(maxcount, right - left + 1)

        return maxcount
