class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num1 = Counter(nums1)
        num2 = Counter(nums2)
        result = []
        for num in num1:
            if num in num2:
                result.extend([num] * min(num1[num], num2[num]))
        
        return result
