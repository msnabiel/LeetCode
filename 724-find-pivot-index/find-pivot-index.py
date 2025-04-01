class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = sum(nums)
        n = len(nums)
        for i in range(len(nums)):
            if i==0:
                leftsum = 0
                rightsum = sum(nums) - nums[i]
                if leftsum == rightsum:
                    pivot = 0
                    return 0
            elif(i==n-1):
                rightsum = 0
                leftsum = summ - nums[i]
                if leftsum == rightsum:
                    return i
            else:
                leftsum = sum(nums[0:i])
                rightsum = sum(nums[i+1:n+1])
                if leftsum == rightsum:
                    return i
        return -1



        