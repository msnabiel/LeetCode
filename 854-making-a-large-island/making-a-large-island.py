class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        island_id = 2
        area_map = {}

        def dfs(i, j, id_):
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = id_
                area = 1
                for x, y in [(0,1), (1,0), (-1,0), (0,-1)]:
                    area += dfs(i + x, j + y, id_)
                return area
            return 0

        # 1. Label each island with a unique ID and compute its area
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j, island_id)
                    area_map[island_id] = area
                    island_id += 1

        # 2. Try changing each 0 to 1 and calculate max possible island size
        max_area = max(area_map.values() or [0])  # If no 1s, default to 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    area = 1
                    for x, y in [(0,1), (1,0), (-1,0), (0,-1)]:
                        ni, nj = i + x, j + y
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            id_ = grid[ni][nj]
                            if id_ not in seen:
                                seen.add(id_)
                                area += area_map[id_]
                    max_area = max(max_area, area)

        return max_area
