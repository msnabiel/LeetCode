class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()  # remove leading spaces
        nstr = ""
        sign_set = False
        for i, ch in enumerate(s):
            if ch in '+-' and not nstr:  # handle sign only at the beginning
                nstr += ch
                sign_set = True
            elif ch.isdigit():
                nstr += ch
            else:
                break
        
        # If nstr is just '+' or '-', it's invalid
        if nstr in ('', '+', '-'):
            return 0
        
        num = int(nstr)
        
        # Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num
