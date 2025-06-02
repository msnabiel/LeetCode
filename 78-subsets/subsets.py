class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(index, path):
            # Add current subset path to result
            res.append(list(path))

            # Explore further elements
            for i in range(index, len(nums)):
                path.append(nums[i])             # Choose
                backtrack(i + 1, path)           # Explore
                path.pop()                       # Un-choose (backtrack)

        backtrack(0, [])
        return res
