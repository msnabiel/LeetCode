from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # Step 1: Add all rotten oranges to queue, count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        # If no fresh oranges, no time needed
        if fresh == 0:
            return 0
        
        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Step 2: BFS to rot fresh oranges
        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
        
        # Step 3: If no fresh left, return minutes else -1
        return minutes if fresh == 0 else -1
