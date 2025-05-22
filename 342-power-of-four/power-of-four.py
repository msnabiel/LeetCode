import math

class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        log_val = math.log(n, 4)
        return log_val.is_integer()