class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        cur_max = cur_min = res = nums[0]

        for num in nums[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max  # swap because negative flips sign

            cur_max = max(num, num * cur_max)
            cur_min = min(num, num * cur_min)

            res = max(res, cur_max)

        return res
