class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        cmax = 0
        for i in s:
            if i == "(":
                count += 1
                cmax = max(cmax,count)
            if i ==")":
                count -= 1
        return cmax
        