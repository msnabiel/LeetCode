class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        L=[]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            L.append(node.val)
            dfs(node.right)
        dfs(root)
        return len(L)
