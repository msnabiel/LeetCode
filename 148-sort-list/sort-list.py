# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        L=[]
        curr = head
        while curr:
            L.append(curr.val)
            curr = curr.next
        L.sort()
        dummy = ListNode(0)
        curr = dummy
        for i in L:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next