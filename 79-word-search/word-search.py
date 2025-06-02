class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r, c, i):
            # Base case: all letters found
            if i == len(word):
                return True
            # Out of bounds or mismatch
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            
            # Mark the cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all 4 directions
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))
            
            # Restore the original value (backtrack)
            board[r][c] = temp
            return found
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
