def removeElements(self, head, val):
        """
        https://leetcode.com/problems/remove-linked-list-elements/submissions/
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr = head
        prev = None
        while curr != None:
            if curr.val == val:
                if prev != None:
                    prev.next = curr.next
                    curr = curr.next
                else:
                    head = curr.next
                    curr = head
                continue
            prev = curr
            curr = curr.next        
        return head
