def reorderList(self, head):
        """
        https://leetcode.com/problems/reorder-list/
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 1 2 3 4 5
        # 1 3 2 4 5
        # 1 3 4 2 5
        # 1 3 4 5 2
        # 1 4 3 5 2
        # 1 4 5 3 2
        # 1 4 5 2 3
        # 1 5 4 2 3
        # 1 5 2 4 3
        if head == None:
            return None
        if head.next == None:
            return head
        prev = head
        curr = head.next
        while curr != None:
            temp_prev = prev
            temp_curr = curr
            prev.next = curr.next
            curr.next = temp_prev
            curr = temp_prev.next
            prev = temp_curr
            curr = temp_prev.next
        # curr = head
        # while curr != None:
        #     print curr.val
        #     curr = curr.next
