class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen_numbers = set() # To store numbers encountered
        
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            temp = 0
            for digit in str(n):
                temp += int(digit) * int(digit)
            n = temp
            
        return n == 1