# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')  # Global max to track the result

        def max_gain(node):
            if not node:
                return 0

            # Max sum on the left and right subtrees; ignore negatives
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Price of the new path (node + left + right)
            price_newpath = node.val + left_gain + right_gain

            # Update global max_sum if new path is better
            self.max_sum = max(self.max_sum, price_newpath)

            # Return max gain including this node to parent
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum

        