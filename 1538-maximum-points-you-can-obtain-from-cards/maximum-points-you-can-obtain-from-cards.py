class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        wlen = n - k
        curr_sum = minsum = sum(cardPoints[:wlen])
        for i in range(wlen,n):
            curr_sum += cardPoints[i] - cardPoints[i-wlen]
            minsum = min(curr_sum,minsum)
        return sum(cardPoints)-minsum