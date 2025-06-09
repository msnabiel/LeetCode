class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len)  # Sort words by increasing length
        dp = {}  # dp[word] = length of longest chain ending at word

        max_chain = 1

        for word in words:
            dp[word] = 1  # At minimum, chain with just this word
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]  # Remove one char
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            max_chain = max(max_chain, dp[word])

        return max_chain
