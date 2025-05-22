class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        max_num = max(nums)
        low, high = 1, max_num
        
        while low <= high:
            mid = (low + high) // 2
            total = 0
            for num in nums:
                total += (num + mid - 1) // mid  # Ceiling division
                if total > threshold:
                    break
            if total <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        
        return low