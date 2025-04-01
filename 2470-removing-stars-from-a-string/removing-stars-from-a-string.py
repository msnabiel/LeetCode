class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            if char == "*":
                if stack:  # Remove the last added character
                    stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack) 



        