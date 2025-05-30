from collections import defaultdict

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count = 0
        prefix_sum = 0
        freq = defaultdict(int)
        freq[0] = 1

        for num in nums:
            prefix_sum += num
            count += freq[prefix_sum - goal]
            freq[prefix_sum] += 1

        return count
