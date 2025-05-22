class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None. Do not return anything, modify nums1 in-place instead.
        """
        # Step 1: Copy only the first m elements
        temp = nums1[:m]

        # Step 2: Add nums2 to the list
        temp += nums2

        # Step 3: Sort the combined list
        temp.sort()

        # Step 4: Update nums1 in-place
        for i in range(len(temp)):
            nums1[i] = temp[i]
