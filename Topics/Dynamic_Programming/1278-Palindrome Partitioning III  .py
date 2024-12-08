class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        def cost(l, r):
            changes = 0
            while l < r:
                if s[l] != s[r]:
                    changes += 1
                l += 1
                r -= 1
            return changes

        cost_matrix = [[0] * n for _ in range(n)]
        for l in range(n):
            for r in range(l, n):
                cost_matrix[l][r] = cost(l, r)

   
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0


        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i):
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost_matrix[p][i - 1])

        return dp[n][k]