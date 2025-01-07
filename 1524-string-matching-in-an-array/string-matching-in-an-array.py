class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        L=[]
        for i in words:
            for j in words:
                if ((i!= j) and (i in j)) and (i  not in L) :
                    L.append(i)

        return L   