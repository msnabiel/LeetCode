import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        nodes = []

        def dfs(node, x, y):
            if not node:
                return
            nodes.append((x, y, node.val))
            dfs(node.left, x - 1, y + 1)
            dfs(node.right, x + 1, y + 1)

        dfs(root, 0, 0)

        # Sort by x (column), then y (row), then val
        nodes.sort()
        
        res = []
        prev_x = float('-inf')
        for x, y, val in nodes:
            if x != prev_x:
                res.append([])
                prev_x = x
            res[-1].append(val)
        
        return res
