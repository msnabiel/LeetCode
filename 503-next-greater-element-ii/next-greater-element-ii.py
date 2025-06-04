class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        L = []
        for i in range(len(nums)):
            flag = False
            for num in nums[i:n+1]:
                if num > nums[i]:
                    L.append(num)
                    flag = True
                    break
            if flag == False:
                for num in nums[:i+1]:
                    if num > nums[i]:
                        L.append(num)
                        flag = True
                        break
            if flag == False:
                L.append(-1)
        return L



            

        