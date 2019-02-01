def deleteNode(self, node):
        """
        https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/
        
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
