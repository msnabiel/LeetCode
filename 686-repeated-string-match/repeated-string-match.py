class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        times = -(-len(b) // len(a))
        temp = a * times

        if b in temp:
            return times

        if b in temp + a:
            return times + 1

        return -1

        

        