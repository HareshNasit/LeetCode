def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Runtime: O(max(m,n)), Space: O(max(m,n))
        curr = l1
        curr1 = l2
        carry = 0
        result = ListNode(0)
        result_curr = result
        while curr or curr1:
            x = 0
            y = 0
            if curr:
                x = curr.val
                curr = curr.next
            if curr1:
                y = curr1.val
                curr1 = curr1.next
            xy_sum = x + y + carry
            carry = xy_sum // 10
            result_curr.next = ListNode(xy_sum%10)
            result_curr = result_curr.next
        if carry > 0:
            result_curr.next = ListNode(carry)
        return result.next
        print(result)


        # Brute Force would be convert both the LLs into string then int
        # and then add and reconvert the sum into a LL.
        # Runtime: O(max(m,n)), Space: O(max(m,n))
