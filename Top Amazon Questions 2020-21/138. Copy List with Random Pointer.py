def copyRandomList(self, head: 'Node') -> 'Node':
        # Runtime: O(n), Space: O(n)
        # Logic: keep a dictionary to check for visited nodes and references.
        # Use Node pointers as keys for the dictionary.
        if head is None:
            return head
        curr = head
        new_head = Node(head.val, None, None)
        new_curr = new_head
        visited_dict = {}
        visited_dict[curr] = new_curr
        while curr:
            if curr.random:
                if curr.random not in visited_dict:
                    new_random = Node(curr.random.val, None, None)
                    visited_dict[curr.random] = new_random
                    new_curr.random = new_random
                else:
                    new_curr.random = visited_dict[curr.random]
            if curr.next:
                if curr.next not in visited_dict:
                    new_next = Node(curr.next.val, None, None)
                    visited_dict[curr.next] = new_next
                    new_curr.next = new_next
                else:
                    new_curr.next = visited_dict[curr.next]
            curr = curr.next
            new_curr = new_curr.next
        return new_head
