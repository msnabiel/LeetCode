class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}  # Using a set for O(1) lookup
        max_count = 0
        current_count = 0
        
        # Count vowels in the first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        
        max_count = current_count
        
        # Slide the window over the rest of the string
        for i in range(k, len(s)):
            # Remove the effect of the character that is leaving the window
            if s[i - k] in vowels:
                current_count -= 1
            # Add the effect of the new character entering the window
            if s[i] in vowels:
                current_count += 1
            
            max_count = max(max_count, current_count)
        
        return max_count
