class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for asteroid in asteroids:
            # Handle collisions
            while stack and asteroid < 0 < stack[-1]:
                # Case 1: right asteroid is smaller -> pop it
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                # Case 2: both are same size -> both explode
                elif stack[-1] == -asteroid:
                    stack.pop()
                # Case 3: right asteroid is bigger -> left asteroid explodes
                break
            else:
                # No collision or all resolved -> push this asteroid
                stack.append(asteroid)

        return stack
