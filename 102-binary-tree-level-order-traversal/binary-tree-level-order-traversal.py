from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            
            for _ in range(level_size):
                curr = queue.popleft()          # dequeue from the left/front
                level_nodes.append(curr.val)    # collect the node's value
                
                if curr.left:
                    queue.append(curr.left)     # enqueue left child
                if curr.right:
                    queue.append(curr.right)    # enqueue right child
            
            result.append(level_nodes)
        
        return result
