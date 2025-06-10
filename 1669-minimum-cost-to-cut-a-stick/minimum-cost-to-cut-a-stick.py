class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        # Add the endpoints 0 and n to the cuts array
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        
        # dp[i][j] = minimum cost to cut the stick between cuts[i] and cuts[j]
        dp = [[0] * m for _ in range(m)]
        
        # For each possible length of segment (number of cuts between i and j)
        for length in range(2, m):  # length is j - i
            for i in range(m - length):
                j = i + length
                dp[i][j] = float('inf')
                
                # Try cutting at each position k between i and j
                for k in range(i + 1, j):
                    # Cost of cutting at k = cost of left part + cost of right part + length of current segment
                    cost = dp[i][k] + dp[k][j] + (cuts[j] - cuts[i])
                    dp[i][j] = min(dp[i][j], cost)
        
        # Return minimum cost to cut the entire stick (from 0 to n)
        return dp[0][m - 1]
        