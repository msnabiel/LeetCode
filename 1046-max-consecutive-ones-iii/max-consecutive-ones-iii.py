class Solution:
    def longestOnes(self, nums, k):
        left = 0
        max_len = 0
        zero_count = 0
        
        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # If we have more than 'k' zeroes, shrink the window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # move the left pointer to the right
            
            # Update the maximum length of the window
            max_len = max(max_len, right - left + 1)
        
        return max_len
