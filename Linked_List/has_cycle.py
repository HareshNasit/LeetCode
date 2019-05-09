 def hasCycle(self, head):
        """
        https://leetcode.com/problems/linked-list-cycle/submissions/
        :type head: ListNode
        :rtype: bool
        """
        nodes = []
        curr = head
        while curr:
            if curr not in nodes:
                print curr.val
                nodes.append(curr)
            else:
                return True
            curr = curr.next
        return False
