from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        freq = Counter(nums)   # Count the frequency of each number
        result = []            # To store elements that appear > n/3 times

        for num in freq:
            if freq[num] > n // 3:
                result.append(num)

        return result
