# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        L=[]
        def pre(root):
            if not root:
                return 
            L.append(root.val)
            pre(root.left)
            pre(root.right)
        pre(root)
        return L