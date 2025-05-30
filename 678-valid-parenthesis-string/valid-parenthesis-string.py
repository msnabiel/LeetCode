class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min_open = 0  # minimum possible '(' count
        max_open = 0  # maximum possible '(' count

        for ch in s:
            if ch == '(':
                min_open += 1
                max_open += 1
            elif ch == ')':
                min_open -= 1
                max_open -= 1
            else:  # ch == '*'
                min_open -= 1    # if '*' is ')'
                max_open += 1    # if '*' is '('

            # Clamp min_open to 0 (we can't have negative open count)
            if min_open < 0:
                min_open = 0

            # If at any point max_open < 0, we have too many ')'
            if max_open < 0:
                return False

        return min_open == 0
