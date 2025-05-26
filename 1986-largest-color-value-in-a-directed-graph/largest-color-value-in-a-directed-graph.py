from typing import List
from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        dp = [[0] * 26 for _ in range(n)]  # dp[node][c]: max count of color c at this node
        visited = [0] * n  # 0 = unvisited, 1 = visiting, 2 = visited
        self.has_cycle = False
        result = 0

        def dfs(node: int) -> List[int]:
            if visited[node] == 1:
                self.has_cycle = True
                return [0] * 26
            if visited[node] == 2:
                return dp[node]

            visited[node] = 1
            color_index = ord(colors[node]) - ord('a')
            count = [0] * 26

            for neighbor in graph[node]:
                neighbor_count = dfs(neighbor)
                if self.has_cycle:
                    return [0] * 26
                for c in range(26):
                    count[c] = max(count[c], neighbor_count[c])

            count[color_index] += 1
            dp[node] = count
            visited[node] = 2
            return count

        for i in range(n):
            if visited[i] == 0:
                counts = dfs(i)
                result = max(result, max(counts))

        return -1 if self.has_cycle else result
