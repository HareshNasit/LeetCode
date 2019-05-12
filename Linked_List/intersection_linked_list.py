def getIntersectionNode(self, headA, headB):
        """
        https://leetcode.com/problems/intersection-of-two-linked-lists/
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        currA = headA
        currB = headB
        lastA = headA
        lastB = headB
        while currA != None or currB != None:
            print currA.val
            print currB.val
            if currA != None:
                currA = currA.next
            else:
                currA = headB
            if currB != None:
                currB = currB.next
            else:
                currB = headA
            if currA != None and currB != None:
                if currA.val == currB.val:
                    return currA
            elif currA == lastA and currB == lastB:
                return None
