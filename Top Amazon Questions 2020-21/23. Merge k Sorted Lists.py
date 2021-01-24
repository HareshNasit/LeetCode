# Runtime: O(n*logk)
    # Space: O(1)
    # Merge with Divide and Conquer
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        interval = 1
        amount = len(lists)
        while interval < amount:
            for i in range(0,amount - interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        if amount > 0:
            return lists[0]
        return None

    def merge2Lists(self, lst1, lst2):
        prehead = ListNode(-1)
        curr1 = lst1
        curr2 = lst2
        new_curr = prehead
        while curr1 and curr2:
            if curr1.val < curr2.val:
                new_curr.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                new_curr.next = ListNode(curr2.val)
                curr2 = curr2.next
            new_curr = new_curr.next
        if curr1:
            new_curr.next = curr1
        if curr2:
            new_curr.next = curr2
        return prehead.next
        # Brute Force
        # Traverse all the elements of the k LLs and append them to
        # an array and sort the array and make a new sorted LL.
        # Runtime: O(nlogn)
        # Space: O(n)

        # all_elems = []
        # for head in lists:
        #     while head:
        #         all_elems.append(head.val)
        #         head = head.next
        # all_elems.sort()
        # if len(all_elems) == 0:
        #     return None
        # new_head = ListNode(all_elems[0])
        # curr = new_head
        # for val in all_elems[1:]:
        #     curr.next = ListNode(val)
        #     curr = curr.next
        # return new_head
