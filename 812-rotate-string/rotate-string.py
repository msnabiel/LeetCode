class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            nstr = s[i:] + s[:i]
            if nstr == goal:
                return True
        return False
