class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L=[]
        for i in set(nums):
            if nums.count(i) == 1:
                L.append(i)
        return sum(L)