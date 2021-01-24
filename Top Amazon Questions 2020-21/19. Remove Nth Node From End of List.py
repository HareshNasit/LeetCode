def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Runtime: O(n), Space: O(1)
        # Logic: Get the total count and subtract n to get the index from start
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        req_index = count - n
        index = 0
        curr = head
        prev = None
        if req_index == 0:
            return head.next
        while curr:
            if req_index == index:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            index += 1
        return head
