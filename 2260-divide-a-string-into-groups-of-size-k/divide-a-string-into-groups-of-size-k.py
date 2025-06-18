class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        L=[]
        for i in range(0,len(s),k):
            L.append(s[i:i+k])
        if len(L[-1]) != k:
            add = k - len(L[-1])
            add = fill*add
            L[-1] = L[-1] + add
        return L