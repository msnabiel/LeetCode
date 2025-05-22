class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(len(str(num))>1):
            nn = 0
            for i in str(num):
                nn += int(i)
            num = nn
        return num