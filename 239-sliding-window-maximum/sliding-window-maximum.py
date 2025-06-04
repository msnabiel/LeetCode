from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if not nums or k == 0:
            return []

        q = deque()
        result = []

        for i in range(n):
            # Remove indices that are out of the current window
            if q and q[0] < i - k + 1:
                q.popleft()

            # Remove from back if current num is greater than the back
            while q and nums[i] > nums[q[-1]]:
                q.pop()

            q.append(i)

            # Append to result if we've hit at least the first window
            if i >= k - 1:
                result.append(nums[q[0]])

        return result
