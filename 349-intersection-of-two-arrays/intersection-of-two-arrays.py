class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num1 = set(nums1)
        num2 = set(nums2)
        L=[]
        for i in num1:
            if i in num2:
                L.append(i)
        return L