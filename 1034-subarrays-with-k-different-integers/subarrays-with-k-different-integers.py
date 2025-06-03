from collections import defaultdict

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atMost(K):
            count = 0
            left = 0
            freq = defaultdict(int)
            for right in range(len(nums)):
                if freq[nums[right]] == 0:
                    K -= 1
                freq[nums[right]] += 1

                while K < 0:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        K += 1
                    left += 1

                count += right - left + 1
            return count

        return atMost(k) - atMost(k - 1)
