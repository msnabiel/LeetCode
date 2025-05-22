class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        total_beauty = 0
        n = len(s)
        
        for i in range(n):
            freq = Counter()
            for j in range(i, n):
                freq[s[j]] += 1
                
                # Use built-ins max() and min() on freq values
                max_freq = max(freq.values())
                min_freq = min(freq.values())
                
                total_beauty += (max_freq - min_freq)
        
        return total_beauty
