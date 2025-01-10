class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        # Step 1: Create a frequency map for the maximum requirements from words2
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char in word_count:
                max_freq[char] = max(max_freq[char], word_count[char])
        
        # Step 2: Check each word in words1
        result = []
        for word in words1:
            word_count = Counter(word)
            # Check if word satisfies all character frequency requirements
            if all(word_count[char] >= max_freq[char] for char in max_freq):
                result.append(word)
        
        return result