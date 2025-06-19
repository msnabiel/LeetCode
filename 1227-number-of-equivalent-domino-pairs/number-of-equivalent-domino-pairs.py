class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
       
        from collections import defaultdict
        freq = defaultdict(int)
        count = 0
        
        for a, b in dominoes:
            key = tuple(sorted((a, b)))  # normalize [2,1] to (1,2)
            count += freq[key]
            freq[key] += 1
        
        return count

