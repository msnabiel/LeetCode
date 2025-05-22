class Solution(object):
    def findCircleNum(self, isConnected):
        def dfs(city):
            visited[city] = True
            for i in range(n):
                if(isConnected[city][i]==1 and visited[i]== False):
                    dfs(i)
        n = len(isConnected)
        provinces = 0
        visited = [False] * n
        for j in range(n):
            if not visited[j]:
                #visited[i] = True
                dfs(j)
                provinces += 1
        return provinces