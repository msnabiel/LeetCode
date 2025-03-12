class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = 0
        pos = 0
        for i in nums:
            if i<0:
                neg+=1
            elif i>0:
                pos = pos + 1
        return max(neg,pos)