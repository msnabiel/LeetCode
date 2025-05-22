class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_count = 0
        additions = 0
        
        for char in s:
            if char == '(':
                open_count += 1
            elif char == ')':
                if open_count > 0:
                    open_count -= 1  # match with an open
                else:
                    additions += 1  # need an extra open
        
        return additions + open_count  # unmatched opens + unmatched closes
