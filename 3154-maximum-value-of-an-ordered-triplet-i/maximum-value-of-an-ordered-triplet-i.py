class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxc = (nums[0] - nums[1]) * nums[2]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if((nums[i] - nums[j]) * nums[k]):
                        count = (nums[i] - nums[j]) * nums[k]
                        if (count > maxc):
                            maxc=count
        if (maxc < 0):
            return 0
        return maxc
        