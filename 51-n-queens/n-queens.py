class Solution(object):
    def solveNQueens(self, n):
        def is_safe(row, col):
            return col not in cols and (row + col) not in diag1 and (row - col) not in diag2
        
        def backtrack(row):
            if row == n:
                board = []
                for r in queens:
                    line = ['.'] * n
                    line[r] = 'Q'
                    board.append("".join(line))
                result.append(board)
                return
            
            for col in range(n):
                if is_safe(row, col):
                    queens.append(col)
                    cols.add(col)
                    diag1.add(row + col)
                    diag2.add(row - col)
                    
                    backtrack(row + 1)
                    
                    # Backtrack
                    queens.pop()
                    cols.remove(col)
                    diag1.remove(row + col)
                    diag2.remove(row - col)
        
        result = []
        queens = []
        cols = set()
        diag1 = set()  # row + col
        diag2 = set()  # row - col
        
        backtrack(0)
        return result
