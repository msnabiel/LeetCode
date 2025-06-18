class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
        