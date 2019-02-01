def removeNthFromEnd(self, head, n):
        """
        https://leetcode.com/problems/remove-nth-node-from-end-of-list/
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list_nodes = []
        curr = head
        length = 0
        while curr != None:
            list_nodes.append(curr)
            curr = curr.next
            length += 1
        if n == length:
            head = head.next 
            return head
        elif n == 0:
            list_nodes[length - 2].next = None
            return head
        prev_node = list_nodes[length - n - 1]
        deleted_node = list_nodes[length - n]
        prev_node.next = deleted_node.next
        
        return head
