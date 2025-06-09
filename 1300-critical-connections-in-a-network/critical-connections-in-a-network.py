class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Initialize discovery and low-link arrays
        disc = [-1] * n     # Discovery time of each node
        low = [-1] * n      # Lowest discovery time reachable
        time = [0]          # Mutable integer to simulate pass-by-reference
        result = []

        def dfs(node, parent):
            disc[node] = low[node] = time[0]
            time[0] += 1

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if disc[neighbor] == -1:  # Not visited
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    # Condition for bridge
                    if low[neighbor] > disc[node]:
                        result.append([node, neighbor])
                else:
                    low[node] = min(low[node], disc[neighbor])

        # Start DFS from node 0
        dfs(0, -1)
        return result
