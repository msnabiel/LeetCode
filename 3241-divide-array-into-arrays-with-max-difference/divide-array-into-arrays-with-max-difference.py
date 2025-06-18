class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # Step 1: Sort the array
        nums.sort()
        
        result = []

        # Step 2: Traverse in steps of 3
        for i in range(0, len(nums), 3):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]

            # Step 3: Check difference between max and min in triplet
            if c - a > k:
                return []

            # Step 4: Append the valid triplet
            result.append([a, b, c])
        
        return result