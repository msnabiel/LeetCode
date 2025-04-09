class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        flip = 0
        # Convert to binary strings, remove '0b', and pad to 32 bits
        bin_a = bin(a)[2:].zfill(32)
        bin_b = bin(b)[2:].zfill(32)
        bin_c = bin(c)[2:].zfill(32)

        # Compare bit by bit
        for i in range(32):
            a_bit = bin_a[i]
            b_bit = bin_b[i]
            c_bit = bin_c[i]

            if c_bit == '0':
                if a_bit == '1':
                    flip += 1
                if b_bit == '1':
                    flip += 1
            else:  # c_bit == '1'
                if a_bit == '0' and b_bit == '0':
                    flip += 1

        return flip
