class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {}
        ops = 0
        
        for num in nums:
            complement = k - num  # Find the complement
            if complement in count and count[complement] > 0:
                ops += 1
                count[complement] -= 1  # Use the complement
            else:
                # If no complement, add the current number to the hashmap
                if num in count:
                    count[num] += 1
                else:
                    count[num] = 1
        
        return ops
