import heapq

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 1:
            return grid[0][0]
        
        # Use Dijkstra's algorithm to find minimum time
        # Priority queue: (time_needed, row, col)
        pq = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while pq:
            time, row, col = heapq.heappop(pq)
            
            # If we reached the destination
            if row == n - 1 and col == n - 1:
                return time
            
            # Skip if already visited
            if (row, col) in visited:
                continue
            
            visited.add((row, col))
            
            # Explore all 4 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check bounds and if not visited
                if (0 <= new_row < n and 0 <= new_col < n and 
                    (new_row, new_col) not in visited):
                    
                    # The time needed is the maximum of current time and the elevation of next cell
                    new_time = max(time, grid[new_row][new_col])
                    heapq.heappush(pq, (new_time, new_row, new_col))
        
        return -1  # Should never reach here for valid input
