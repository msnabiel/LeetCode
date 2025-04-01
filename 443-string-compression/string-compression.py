class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0  # Pointer to write the compressed string
        read = 0   # Pointer to traverse the chars array
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Count consecutive occurrences of the character
            while read < len(chars) and chars[read] == char:
                count += 1
                read += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write  # New length of the modified list
