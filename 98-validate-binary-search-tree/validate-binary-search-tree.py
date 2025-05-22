# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        L=[]
        def inorder(root):
            if not root:  # base case
                return
            inorder(root.left)
            L.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(len(L)-1):
            if L[i] >= L[i+1]:
                return False
        return True
                
