class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                # Check left neighbor (or assume it's 0 if i == 0)
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                # Check right neighbor (or assume it's 0 if i == last index)
                right_empty = (i == length - 1 or flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:
                    flowerbed[i] = 1  # Plant the flower
                    count += 1
                    if count >= n:  # If we've placed enough, return True
                        return True
        
        return count >= n  # Check if we planted enough flowers
