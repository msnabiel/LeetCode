class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sort(lo, hi):
            if lo >= hi: return 0
            mid = (lo + hi) // 2
            count = sort(lo, mid) + sort(mid + 1, hi)
            j = mid + 1
            for i in range(lo, mid + 1):
                while j <= hi and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            nums[lo:hi + 1] = sorted(nums[lo:hi + 1])
            return count
        return sort(0, len(nums) - 1)

        