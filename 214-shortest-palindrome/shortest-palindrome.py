class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        rev = s[::-1]
        
        # Find the longest prefix of s which is a palindrome
        for i in range(len(s)):
            if s.startswith(rev[i:]):
                # We found the longest palindromic prefix
                return rev[:i] + s
        
        return ""  # Should never reach here
