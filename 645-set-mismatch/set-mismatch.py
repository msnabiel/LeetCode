class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n, a, b = len(nums), sum(nums), sum(set(nums))
		
        s = n*(n+1)//2
        
        return [a-b, s-b]