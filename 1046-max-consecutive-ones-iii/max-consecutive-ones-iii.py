class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numberZeros = 0
        l = 0
        for r in nums:
            if r == 0:
                numberZeros += 1
            if numberZeros > k:
                if nums[l] == 0:
                    numberZeros -= 1
                l += 1
        return len(nums) - l
