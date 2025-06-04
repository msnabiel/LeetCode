class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        arr = [nums.pop(0)]                  # <-- 1) initial step
 
        for n in nums:                       # <-- 2) iterate through nums
            
            if n > arr[-1]:                  # <--    2a)
                arr.append(n)

            else:                            # <--    2b)
                arr[bisect_left(arr, n)] = n 

        return len(arr)                      # <-- 3) return the length of arr
        