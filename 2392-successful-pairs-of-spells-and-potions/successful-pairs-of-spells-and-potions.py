class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        result=[]
        for spell in spells:
            # Minimum required potion value to be successful
            min_potion = (success + spell - 1) // spell  # Equivalent to ceil(success / spell)
            
            # Find the first index where potion >= min_potion using binary search
            index = bisect.bisect_left(potions, min_potion)
            
            # The count of successful pairs is the number of potions from `index` to end
            result.append(len(potions) - index)

        return result