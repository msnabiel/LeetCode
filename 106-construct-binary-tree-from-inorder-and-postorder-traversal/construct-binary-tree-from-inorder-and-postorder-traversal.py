# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None

        # Hashmap for quick lookup of index in inorder
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None

            # Last element in postorder is the root
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Get index of root in inorder
            index = inorder_index_map[root_val]

            # Build right subtree first (important!)
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)

            return root

        return helper(0, len(inorder) - 1)