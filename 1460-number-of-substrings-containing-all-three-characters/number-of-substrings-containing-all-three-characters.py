class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        res = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # While we have at least one of each 'a', 'b', and 'c'
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                res += len(s) - right  # All substrings from current right to end are valid
                count[s[left]] -= 1
                left += 1

        return res

