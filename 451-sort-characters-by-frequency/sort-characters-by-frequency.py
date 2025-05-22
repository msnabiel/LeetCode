class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        
        # Count frequency of each character
        freq = Counter(s)
        
        # Sort characters by frequency in descending order
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Build the result string
        result = []
        for char, count in sorted_chars:
            result.append(char * count)
        
        return ''.join(result)
