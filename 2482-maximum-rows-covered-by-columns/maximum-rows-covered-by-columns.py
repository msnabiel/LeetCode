class Solution(object):
    def maximumRows(self, matrix, numSelect):
        """
        :type matrix: List[List[int]]
        :type numSelect: int
        :rtype: int
        """
        rows = len(matrix)
        columns = len(matrix[0])

        zero_rows = 0
        non_zero_rows = []
        # Step 1: Count rows that are all zeros (already covered)
        for i in range(rows):
            if matrix[i].count(1) == 0:
                zero_rows += 1
            else:
                non_zero_rows.append(matrix[i])
        # Step 2: For each combination of numSelect columns, count covered rows
        from itertools import combinations
        max_cover = 0
        for cols_selected in combinations(range(columns), numSelect):
            selected = set(cols_selected)
            covered = 0
            for row in non_zero_rows:
                # If all 1s in the row are within the selected columns
                if all(j in selected for j, val in enumerate(row) if val == 1):
                    covered += 1
            max_cover = max(max_cover, covered)

        return zero_rows + max_cover

                