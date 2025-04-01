from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if set(word1) != set(word2):
            return False
        a = Counter(word1)
        b = Counter(word2)
        return sorted(a.values()) == sorted(b.values())
        