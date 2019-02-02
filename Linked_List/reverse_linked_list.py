def reverseList(self, head):
        """
        https://leetcode.com/problems/reverse-linked-list/submissions/
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None
        next = None
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
