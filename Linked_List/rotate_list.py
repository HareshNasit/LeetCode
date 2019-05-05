def rotateRight(self, head, k):
        """
        https://leetcode.com/problems/rotate-list/
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        #Brute Force O(n*k)
        # if head == None:
        #     return head
        # count = 0
        # while count < k:
        #     last_node = None
        #     curr = head
        #     prev = None
        #     while curr.next != None:
        #         prev = curr
        #         curr = curr.next
        #     if prev == None:
        #         return head
        #     last_node = curr
        #     prev.next = None
        #     last_node.next = head
        #     head = last_node
        #    # self.print_elements(head)
        #     count += 1
        # return head
