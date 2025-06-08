from collections import Counter 
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Step 1: Count frequencies
        freq = Counter(tasks)
        max_freq = max(freq.values())
        
        # Step 2: Count how many tasks have max frequency
        # Initialize max_count to 0
        max_count = 0

        # Loop through each key (task) in the frequency dictionary
        for task in freq:
            # Check if the frequency of this task equals the max frequency
            if freq[task] == max_freq:
                # If so, increment the max_count
                max_count = max_count + 1

        # Step 3: Calculate result
        part_count = max_freq - 1
        part_length = n + 1
        empty_slots = part_count * part_length + max_count
        
        return max(len(tasks), empty_slots)
