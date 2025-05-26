from collections import deque

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m, n = len(heights), len(heights[0])

        def canReach(threshold):
            visited = [[False]*n for _ in range(m)]
            queue = deque([(0, 0)])
            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            while queue:
                x, y = queue.popleft()
                if x == m - 1 and y == n - 1:
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        if abs(heights[nx][ny] - heights[x][y]) <= threshold:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            return False

        # Binary search over effort value
        left, right = 0, 10**6
        while left < right:
            mid = (left + right) // 2
            if canReach(mid):
                right = mid
            else:
                left = mid + 1
        return left
