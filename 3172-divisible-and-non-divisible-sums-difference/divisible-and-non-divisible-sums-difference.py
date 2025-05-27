class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # Sum of all numbers from 1 to n
        total = n * (n + 1) // 2
        
        # Sum of all numbers from 1 to n divisible by m
        count = n // m
        div_sum = m * count * (count + 1) // 2
        
        return total - 2 * div_sum
