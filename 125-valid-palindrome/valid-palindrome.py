class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = ''
        for c in s:
            if c.isalnum():
                temp += c.lower()
        return temp == temp[::-1]
