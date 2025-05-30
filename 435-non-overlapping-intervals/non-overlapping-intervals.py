class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])  # sort by end time
        end = float('-inf')
        count = 0
        
        for i in intervals:
            if i[0] >= end:
                end = i[1]  # no overlap, update end
            else:
                count += 1  # overlap, need to remove one

        return count
