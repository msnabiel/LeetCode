class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Modifies nums in-place.
        """
        x = nums.count(0)  # Count zeroes
        
        nums[:] = [num for num in nums if num != 0]  # Keep only non-zero elements
        
        nums.extend([0] * x)  # Append required number of zeroes
