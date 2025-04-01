class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0  # Two pointers: i for s, j for t
        
        while j < len(t) and i < len(s):
            if s[i] == t[j]:  # If characters match, move pointer i in s
                i += 1
            j += 1  # Always move pointer j in t
        
        return i == len(s)  # If i reached the end of s, s is a subsequence
