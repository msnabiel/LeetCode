class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        total = 0

        # Reuse matrix as dp table to save space
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i > 0 and j > 0:
                        matrix[i][j] = 1 + min(
                            matrix[i-1][j],
                            matrix[i][j-1],
                            matrix[i-1][j-1]
                        )
                    total += matrix[i][j]
        return total
