class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        tpse = Counter(zip(*grid))                  # <-- determine the transpose
                                                    #     and hash the rows

        grid = Counter(map(tuple,grid))             # <-- hash the rows of grid. (Note the tuple-map, so
                                                    #     we can compare apples w/ apples in next step.)

        return  sum(tpse[t]*grid[t] for t in tpse)  # <
            

        