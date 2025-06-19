class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans = 1
        min_val = nums[0]
        for num in nums[1:]:
            if num - min_val > k:
                ans += 1
                min_val = num
        return ans
        