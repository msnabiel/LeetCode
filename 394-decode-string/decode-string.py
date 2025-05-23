class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack =[]
        for i in range(len(s)):
            if s[i]!="]": 
                stack.append(s[i])
            else:
                substr="" #to store the substrings
                while stack[-1]!="[": 
                    substr=stack.pop()+substr 
                stack.pop()
                k="" #to store the integer value
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                stack.append(int(k)*substr)
        return "".join(stack)

        