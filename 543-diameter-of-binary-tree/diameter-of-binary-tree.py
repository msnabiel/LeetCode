# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update max diameter at this node
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return height of subtree rooted at this node
            return max(left_height, right_height) + 1
        
        height(root)
        return self.max_diameter
