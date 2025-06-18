class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = 0
        s = s.split("|")
        for i in range(0,len(s),2):
            temp += s[i].count("*")
        return temp