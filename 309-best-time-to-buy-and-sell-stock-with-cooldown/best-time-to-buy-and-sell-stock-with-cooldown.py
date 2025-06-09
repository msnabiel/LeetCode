class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        n = len(prices)
        hold = -prices[0]
        sold = 0
        rest = 0
        
        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest
            
            hold = max(prev_hold, prev_rest - price)  # buy or keep holding
            sold = prev_hold + price                  # sell today
            rest = max(prev_rest, prev_sold)          # stay in rest

        return max(sold, rest)  # can't end with holding
