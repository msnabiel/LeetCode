class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        result = 0
        prev_less = [None] * n
        next_less = [None] * n

        # Previous Less Element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)

        # Reset stack for Next Less Element
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_less[i] = stack[-1] if stack else n
            stack.append(i)

        for i in range(n):
            left = i - prev_less[i]
            right = next_less[i] - i
            result += arr[i] * left * right
            result %= MOD

        return result
