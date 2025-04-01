class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        L=[0]
        for i in gain:
            x = L[-1] + i
            L.append(x)
        return max(L)

        