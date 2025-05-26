# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        L = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            L.append(node.val)
            inorder(node.right)

        inorder(root)

        seen = set()
        for val in L:
            if k - val in seen:
                return True
            seen.add(val)

        return False
