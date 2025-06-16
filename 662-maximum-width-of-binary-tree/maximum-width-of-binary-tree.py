# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        max_width = 0
        queue = deque([(root, 0)])  # (node, index)

        while queue:
            level_length = len(queue)
            _, first_index = queue[0]

            for i in range(level_length):
                node, index = queue.popleft()
                # Normalize the index to prevent overflow
                index -= first_index

                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))

                if i == level_length - 1:
                    # Last node of the level
                    max_width = max(max_width, index + 1)

        return max_width
