class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        diff = float('-inf')
        for i in range(n):
            if i == n-1:
                if abs(nums[i] - nums[0]) > diff:
                    diff = abs(nums[i] - nums[0])
            elif abs(nums[i] - nums[i+1]) > diff:
                diff = abs(nums[i] - nums[i+1])
        return diff
            
        