class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
        L= []
        index = nums.index(target)
        rnums = sorted(nums,reverse = True)
        lindex = rnums.index(target)
        lindex = len(nums) - lindex - 1
        L.append(index)
        L.append(lindex)
        return L
        