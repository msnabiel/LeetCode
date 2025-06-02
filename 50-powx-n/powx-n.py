class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = x**n
        if ans >= 2**31 -1:
            return 2**31 -1
        elif ans < -2**31:
            return -2**31
        else:
            return ans
        