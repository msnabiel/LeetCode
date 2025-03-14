class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        if sum(candies) < k:
            return 0  # Not enough candies to give at least one to each child

        left, right = 1, max(candies)
        best = 0

        while left <= right:
            mid = (left + right) // 2
            count = sum(c // mid for c in candies)  # Number of children we can serve

            if count >= k:  # Can serve at least k children
                best = mid
                left = mid + 1
            else:
                right = mid - 1

        return best

        
        