class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s) - 1, 0, -1):
            if s.startswith(s[:i]) and s.endswith(s[:i]):
                return s[:i]
        return ""
        