from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        visit = set()         # nodes fully visited
        count = set()         # nodes in current DFS path (for cycle detection)
        res = []              # result list

        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)  # src → dst (src must come before dst)

        def dfs(node):
            if node in count:   # cycle detected
                return False
            if node in visit:   # already processed
                return True

            count.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            count.remove(node)

            visit.add(node)
            res.append(node)
            return True

        for i in range(numCourses):
            if i not in visit:
                if not dfs(i):
                    return []

        return res