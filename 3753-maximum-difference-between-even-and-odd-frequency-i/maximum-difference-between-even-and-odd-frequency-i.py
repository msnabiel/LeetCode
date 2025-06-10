class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = Counter(s)
        odd = []
        even = []
        for num in temp.values():
            if num % 2 != 0:
                odd.append(num)
            else:
                even.append(num)
        return max(odd) - min(even)