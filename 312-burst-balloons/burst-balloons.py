class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Add boundary balloons with value 1
        # This simplifies boundary checking
        balloons = [1] + nums + [1]
        n = len(balloons)
        
        # dp[i][j] = maximum coins we can get by bursting all balloons 
        # in the open interval (i, j), i.e., balloons i+1, i+2, ..., j-1
        dp = [[0] * n for _ in range(n)]
        
        # length is the length of the interval we're considering
        # We start from length 2 (empty interval) and go up to n-1
        for length in range(2, n):
            # i is the left boundary, j is the right boundary
            for i in range(n - length):
                j = i + length
                
                # Try bursting each balloon k in the interval (i, j) as the LAST one
                # When k is the last balloon to burst in (i, j), 
                # its neighbors are balloons[i] and balloons[j]
                for k in range(i + 1, j):
                    # Coins from bursting balloon k last = balloons[i] * balloons[k] * balloons[j]
                    # Plus coins from left subproblem (i, k) and right subproblem (k, j)
                    coins = balloons[i] * balloons[k] * balloons[j] + dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], coins)
        
        # Return the maximum coins for the entire array (excluding boundaries)
        return dp[0][n - 1]
