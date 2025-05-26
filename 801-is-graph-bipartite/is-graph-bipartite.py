from collections import defaultdict, deque

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        adj = defaultdict(list)
        
        # Build adjacency list from graph
        for src in range(n):
            for dst in graph[src]:
                adj[src].append(dst)
        
        color = {}  # node -> 0 or 1

        # For each node (handle disconnected components)
        for node in range(n):
            if node not in color:
                # BFS from this node
                queue = deque([node])
                color[node] = 0

                while queue:
                    current = queue.popleft()
                    for neighbor in adj[current]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            return False
        return True
