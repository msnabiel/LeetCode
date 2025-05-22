# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        # Check if it's a leaf node and the sum matches
        if not root.left and not root.right:
            return targetSum == root.val

        # Recurse left and right with reduced target sum
        remainingSum = targetSum - root.val
        return (
            self.hasPathSum(root.left, remainingSum) or
            self.hasPathSum(root.right, remainingSum)
        )