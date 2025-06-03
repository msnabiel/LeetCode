class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        max_area = 0
        n_cols = len(matrix[0])
        heights = [0] * (n_cols + 1)  # extra 0 at end to force cleanup

        for row in matrix:
            for i in range(n_cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

            # Stack-based histogram max area
            stack = []
            for i in range(n_cols + 1):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * width)
                stack.append(i)

        return max_area
