class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        s = title.split()
        for i in range(len(s)):
            if (len(s[i]) == 1) or (len(s[i]) == 2):
                s[i] = s[i].lower()
            else:
                s[i] = s[i][0].upper() + s[i][1:].lower()
                
        return ' '.join(s)
