class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        for i in range(1,num+1):
            temp = 0
            for j in str(i):
                temp += int(j)
            if temp % 2 == 0:
                count += 1
        return count