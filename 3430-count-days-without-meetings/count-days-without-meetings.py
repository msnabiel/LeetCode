class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        if not meetings:
            return days  # If no meetings, all days are unoccupied
        
        # Step 1: Sort meetings by start day
        meetings.sort()
        
        # Step 2: Merge overlapping intervals and count occupied days
        total_occupied = 0
        prev_start, prev_end = meetings[0]  # First meeting's range
        
        for i in range(1, len(meetings)):
            curr_start, curr_end = meetings[i]
            
            # If overlapping, merge
            if curr_start <= prev_end:
                prev_end = max(prev_end, curr_end)
            else:
                # No overlap, add previous range to occupied days
                total_occupied += (prev_end - prev_start + 1)
                prev_start, prev_end = curr_start, curr_end

        # Step 3: Add last merged interval
        total_occupied += (prev_end - prev_start + 1)

        # Step 4: Compute and return unoccupied days
        return days - total_occupied
