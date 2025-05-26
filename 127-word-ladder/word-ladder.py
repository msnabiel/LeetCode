from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        queue = deque()
        queue.append((beginWord, 1))  # (current_word, depth)

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps

            # Try changing each letter in the word
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append((next_word, steps + 1))

        return 0  # no path found
