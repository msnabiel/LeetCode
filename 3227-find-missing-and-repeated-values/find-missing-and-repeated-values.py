class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        total_elements = n * n
        L = []
        output = []
        
        # Flatten the 2D grid into a 1D list
        for i in range(n):
            for j in range(n):
                L.append(grid[i][j])
        
        # Find the repeated number
        repeated = None
        for num in L:
            if L.count(num) > 1:
                repeated = num
                break
        
        # Find the missing number
        for i in range(1, total_elements + 1):
            if i not in L:
                missing = i
                break
        
        output.append(repeated)
        output.append(missing)
        
        return output
