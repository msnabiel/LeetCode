class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if(len(nums)) == 1:
            return 0
        if(len(nums)) == 2:
            if nums[1] > nums[0]:
                return 1
            else:
                return 0
        if nums[n-1] > nums[n-2]:
            return n - 1
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1]:
                if nums[i] > nums[i+1]:
                    return i
        return 0