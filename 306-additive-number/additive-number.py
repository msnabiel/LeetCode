class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        n = len(num)

        # Try all possible first and second number splits
        for i in range(1, n):
            for j in range(i + 1, n):
                num1 = num[:i]
                num2 = num[i:j]

                # Skip if there's a leading zero (but allow "0" itself)
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue

                a, b = int(num1), int(num2)
                k = j
                while k < n:
                    c = a + b
                    c_str = str(c)
                    if not num.startswith(c_str, k):
                        break
                    k += len(c_str)
                    a, b = b, c

                if k == n:
                    return True  # Successfully used whole string

        return False
