class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        L=[]
        summ = max(candies)
        for i in candies:
            if(i+extraCandies>=summ):
                L.append(True)
            else:
                L.append(False)
        return L
        