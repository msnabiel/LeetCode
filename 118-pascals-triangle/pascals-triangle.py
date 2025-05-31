class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        L = []

        for i in range(numRows):
            if i == 0:
                L.append([1])
            else:
                row = [1]
                for j in range(1, i):
                    row.append(L[i-1][j-1] + L[i-1][j])
                row.append(1)
                L.append(row)
        
        return L
