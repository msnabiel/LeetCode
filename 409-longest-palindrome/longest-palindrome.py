from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sc = Counter(s)
        length = 0
        has_odd = False # Flag to check if we can add a single character in the middle

        for count in sc.values():
            # Add all pairs
            length += (count // 2) * 2
            # If a character has an odd count, we can potentially use one of them
            # in the middle of the palindrome. We only need one such character.
            if count % 2 == 1:
                has_odd = True
        
        # If there was at least one character with an odd count, 
        # we can add 1 to the total length for the middle character.
        if has_odd:
            length += 1
            
        return length