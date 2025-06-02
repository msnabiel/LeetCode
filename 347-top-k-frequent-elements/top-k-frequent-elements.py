from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)               # Count frequency of each element
        most_common = count.most_common(k) # Get k most common (element, frequency) pairs
        return [elem for elem, freq in most_common]  # Return elements only
