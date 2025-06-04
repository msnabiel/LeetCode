class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def backtrack(row):
            if row == n:
                board = []
                for i in range(n):
                    row_str = ['.'] * n
                    row_str[queens[i]] = 'Q'
                    board.append("".join(row_str))
                result.append(board)
                return

            for col in range(n):
                if col in cols or (row - col) in neg_diag or (row + col) in pos_diag:
                    continue

                queens[row] = col
                cols.add(col)
                neg_diag.add(row - col)
                pos_diag.add(row + col)

                backtrack(row + 1)

                # Backtrack
                cols.remove(col)
                neg_diag.remove(row - col)
                pos_diag.remove(row + col)
                queens[row] = -1

        result = []
        queens = [-1] * n  # queens[i] = column where queen is placed in row i
        cols = set()
        pos_diag = set()  # (row + col)
        neg_diag = set()  # (row - col)
        backtrack(0)
        return len(result)
        