class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = int(a,2)
        d = int(b,2)
        return bin(c+d)[2:]

        