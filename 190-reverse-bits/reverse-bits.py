class Solution:
    def reverseBits(self, n):
        # Convert to 32-bit binary string
        bin_str = '{:032b}'.format(n)
        
        # Reverse the string
        reversed_str = bin_str[::-1]
        
        # Debug print
        print("Original binary:  ", bin_str)
        print("Reversed binary:  ", reversed_str)

        # Convert back to integer
        return int(reversed_str, 2)
