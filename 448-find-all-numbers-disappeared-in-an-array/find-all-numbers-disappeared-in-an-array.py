class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        num_set = set(nums)
        L = []
        for i in range(1, n + 1):
            if i not in num_set:
                L.append(i)
        return L

        
        