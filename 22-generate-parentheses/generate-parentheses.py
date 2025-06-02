class Solution(object):
    def generateParenthesis(self, n):
        def generate(curr, open_count, close_count):
            # Base case: when the string is complete
            if len(curr) == 2 * n:
                return [curr]

            result = []

            # Add '(' if we have not used all n opens
            if open_count < n:
                result += generate(curr + "(", open_count + 1, close_count)

            # Add ')' if it won't break validity
            if close_count < open_count:
                result += generate(curr + ")", open_count, close_count + 1)

            return result

        return generate("", 0, 0)
