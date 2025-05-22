# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        L=[]
        def post(root):
            if not root:
                return
            post(root.left)
            post(root.right)
            L.append(root.val)
        post(root)
        return L