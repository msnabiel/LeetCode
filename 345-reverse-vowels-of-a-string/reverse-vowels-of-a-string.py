class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        V=['a','e','i','o','u','A','E','I','O','U']
        L=[]
        s=list(s)
        for i in s:
            if i in V:
                L.append(i)
        L.reverse()
        count = 0
        for i in range(len(s)):
            if s[i] in V:
                s[i] = L[count]
                count +=1
        return "".join(s)

        