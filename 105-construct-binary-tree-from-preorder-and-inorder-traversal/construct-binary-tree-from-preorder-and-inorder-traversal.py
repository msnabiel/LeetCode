# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None

        # Build a value->index map for inorder traversal
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Index pointer to current root in preorder traversal
        self.pre_idx = 0

        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            # Pick the root value from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Find the root in inorder
            index = inorder_index_map[root_val]

            # Build left and right subtree
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)

            return root

        return helper(0, len(inorder) - 1)
