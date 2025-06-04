class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = s.split()
        print(L)
        for i in range(len(L)):
            L[i] = L[i][::-1] 
        return " ".join(L)