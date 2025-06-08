class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        L=[]
        for i in range(1,n+1):
            L.append(str(i))
        L.sort()
        for j in range(len(L)):
            L[j] = int(L[j])
        return L