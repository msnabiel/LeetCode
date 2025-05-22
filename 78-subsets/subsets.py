class Solution(object):
    def subsets(self, nums):
        result = []
        subset = []
        
        def backtrack(start):
            # Add a copy of current subset to results
            result.append(subset[:])
            
            for i in range(start, len(nums)):
                # Include nums[i]
                subset.append(nums[i])
                # Recurse with next elements
                backtrack(i + 1)
                # Backtrack: remove nums[i]
                subset.pop()
        
        backtrack(0)
        return result
