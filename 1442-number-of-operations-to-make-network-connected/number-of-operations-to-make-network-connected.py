class Solution(object):
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1
            
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        components = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1

        return components - 1
