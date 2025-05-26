from collections import defaultdict

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        adj = defaultdict(list)
        
        # Build adjacency list
        for src in range(n):
            for dst in graph[src]:
                adj[src].append(dst)
        
        color = {}

        def dfs(node, c):
            color[node] = c
            for neighbor in adj[node]:
                if neighbor not in color:
                    if not dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == color[node]:
                    return False
            return True

        for node in range(n):
            if node not in color:
                if not dfs(node, 0):
                    return False

        return True
