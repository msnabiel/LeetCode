class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)
