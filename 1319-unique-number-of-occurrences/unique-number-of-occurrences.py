class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s=set()
        m = set()
        for i in arr:
            s.add(arr.count(i))
            m.add(i)
        print(s)
        if len(s) == len(m):
            return True
        else:
            return False
        