def deleteDuplicates(self, head):
        """
        https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
        
        :type head: ListNode
        :rtype: ListNode
        """
        unique = []
        curr = head
        prev = None
        while curr != None:
            if curr.val in unique:
                prev.next = curr.next
                curr = curr.next
            else:
                unique.append(curr.val)
                prev = curr
                curr = curr.next
        return head
