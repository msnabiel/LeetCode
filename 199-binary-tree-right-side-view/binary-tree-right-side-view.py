class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def preorder(node, depth):
            if not node:
                return
            if depth == len(result):
                result.append(node.val)
            preorder(node.right, depth + 1)
            preorder(node.left, depth + 1)

        preorder(root, 0)
        return result
