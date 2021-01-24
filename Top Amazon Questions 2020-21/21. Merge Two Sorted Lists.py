def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Brute force method, traverse all the elements and store them in an
        # arraylist and then create a new LinkedList. Runtime: O((m+n)*log(m+n)).

        # Recursive
        # Runtime: O(m+n) because each recursive call increments the pointer to
        # either l1 or l2 and eventually traverses all the elements.
        # Space: O(m+n) since its recursion and the first recursive call
        # does not return untill all the elements are traveresed
        # if l1 is None:
        #     return l2
        # elif l2 is None:
        #     return l1
        # else:
        #     if l1.val < l2.val:
        #         l1.next = self.mergeTwoLists(l1.next, l2)
        #         return l1
        #     else:
        #         l2.next = self.mergeTwoLists(l1, l2.next)
        #         return l2

        # Iterative Approach
        # Runtime: O(m+n) since we traverse each element once
        # Space: O(1) since we make use of the given l1 and l2 and do not use
        # any new variables.
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        if l1:
            prev.next = l1
        else:
            prev.next = l2
        return prehead.next
