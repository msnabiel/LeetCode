# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Save next node
            current.next = prev       # Reverse current node's pointer
            prev = current            # Move prev forward
            current = next_node       # Move current forward
        
        return prev  # New head of the reversed list