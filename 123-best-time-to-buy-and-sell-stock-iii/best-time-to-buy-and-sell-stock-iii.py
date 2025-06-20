class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for price in prices:
            buy1 = max(buy1, -price)            # First buy
            sell1 = max(sell1, buy1 + price)    # First sell
            buy2 = max(buy2, sell1 - price)     # Second buy
            sell2 = max(sell2, buy2 + price)    # Second sell

        return sell2
