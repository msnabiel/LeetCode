class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Compute the initial sum of the first k elements
        max_sum = sum(nums[:k])
        window_sum = max_sum
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]  # Add new element, remove old
            max_sum = max(max_sum, window_sum)
        
        return float(max_sum) / k  # Return max average
