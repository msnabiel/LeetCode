class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        import math
        log_n = math.log(n,3)
        return abs(round(log_n) - log_n) < 1e-10