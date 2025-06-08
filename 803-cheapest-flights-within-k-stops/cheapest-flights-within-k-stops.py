import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Build graph
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # Priority queue: (cost, current_city, stops)
        heap = [(0, src, 0)]

        # Use a dictionary to keep track of visited nodes with minimum stops
        visited = dict()

        while heap:
            cost, city, stops = heapq.heappop(heap)

            # If destination is reached within k+1 moves (k stops = k+1 edges)
            if city == dst:
                return cost

            # If we have visited this city with fewer stops, skip
            if (city in visited and visited[city] <= stops):
                continue
            visited[city] = stops

            if stops <= k:
                for neighbor, price in graph[city]:
                    heapq.heappush(heap, (cost + price, neighbor, stops + 1))

        return -1
