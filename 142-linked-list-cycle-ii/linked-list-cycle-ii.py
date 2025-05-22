class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Step 2: Find the start of the cycle
                pointer = head
                while pointer != slow:
                    pointer = pointer.next
                    slow = slow.next
                return pointer  # Start of cycle

        return None  # No cycle
