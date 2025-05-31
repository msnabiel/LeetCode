from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        if s == t:
            return t
        if not s or not t:
            return ""
        need = Counter(t)
        window = {}
        l = 0
        have = 0
        res, length = [-1,-1],float('inf')
        for r in range(len(s)):
            char = s[r]
            window[char]= window.get(char,0) + 1
            if char in need and window[char] == need[char]:
                have += 1
            while have == len(need):
                if r-l+1 < length:
                    res = [l,r]
                    length = r - l + 1
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if length != float('inf') else ""

                    


            