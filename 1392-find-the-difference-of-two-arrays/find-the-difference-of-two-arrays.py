class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        L=[]
        M=[]
        O=[]
        for i in nums1:
            if i not in nums2:
                if i not in L:
                    L.append(i)
        for j in nums2:
            if j not in nums1:
                if j not in M:
                    M.append(j)
        O.append(L)
        O.append(M)
        return O
        