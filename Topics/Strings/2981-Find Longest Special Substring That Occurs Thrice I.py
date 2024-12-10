class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_valid(length):
            substring_count = {}
            for i in range(len(s) - length + 1):
                substring = s[i:i + length]
                if len(set(substring)) == 1:  
                    substring_count[substring] = substring_count.get(substring, 0) + 1
                    if substring_count[substring] >= 3:
                        return True
            return False

        low, high = 1, len(s)
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if is_valid(mid):
                result = mid  
                low = mid + 1 
            else:
                high = mid - 1  
        
        return result