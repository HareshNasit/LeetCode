def oddEvenList(self, head):
        """
        https://leetcode.com/problems/odd-even-linked-list/
        :type head: ListNode
        :rtype: ListNode
        """
        def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        odd = head
        even = head.next
        even_head = even
        while even != None and even.next != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

        #Brute Force
        """count = 1
        curr = head
        odd_lst = ListNode(0)
        odd_curr = odd_lst
        even_lst = ListNode(0)
        even_curr = even_lst
        last_node = None
        while curr != None:
            if count % 2 == 0:
                even_curr.next = curr
                even_curr = even_curr.next
            else:
                odd_curr.next = curr
                odd_curr = odd_curr.next
                last_node = curr
            curr = curr.next
            count += 1
        odd_lst = odd_lst.next
        last_node.next = even_lst.next
        return odd_lst"""
