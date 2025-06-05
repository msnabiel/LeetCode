class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
            """
        parent = {}

        # Initialize parent of each char to itself
        for c in 'abcdefghijklmnopqrstuvwxyz':
            parent[c] = c

        def find(c):
            if parent[c] != c:
                parent[c] = find(parent[c])  # Path compression
            return parent[c]

        def union(c1, c2):
            p1, p2 = find(c1), find(c2)
            if p1 == p2:
                return
            # Always make the smaller character the root
            if p1 < p2:
                parent[p2] = p1
            else:
                parent[p1] = p2

        # Build equivalence classes
        for a, b in zip(s1, s2):
            union(a, b)

        # Convert baseStr
        return ''.join(find(c) for c in baseStr)

            