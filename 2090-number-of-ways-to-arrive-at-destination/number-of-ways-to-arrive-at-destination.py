import heapq

class Solution(object):
    def countPaths(self, n, roads):
        MOD = 10**9 + 7
        
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        heap = [(0, 0)]  # (distance, node)
        
        while heap:
            d, u = heapq.heappop(heap)
            
            if d > dist[u]:
                continue
            
            for v, time in graph[u]:
                if d + time < dist[v]:
                    dist[v] = d + time
                    ways[v] = ways[u]
                    heapq.heappush(heap, (dist[v], v))
                elif d + time == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        
        return ways[n - 1]
