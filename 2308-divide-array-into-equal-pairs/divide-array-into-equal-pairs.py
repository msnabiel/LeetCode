class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}
        for item in nums:
            count[item] = count.get(item, 0) + 1
        for item in nums:
            if((count[item]%2) != 0):
                return False
        return True
            
        