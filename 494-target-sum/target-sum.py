class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum = sum(nums)
        
        # Check for impossible case
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0
        
        subset_sum = (total_sum + target) // 2
        
        # dp[i] will be the number of ways to get sum i
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # One way to make sum 0: choose nothing

        for num in nums:
            # Iterate backwards to avoid using the same number more than once
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_sum]
