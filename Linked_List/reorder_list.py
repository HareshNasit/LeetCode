 def reorderList(self, head):
        """
        https://leetcode.com/problems/reorder-list/
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        """ Runtime O(n)
        Strategy: Get the middle element of the LL and reverse the right side and 
        the left side of the middle element except the head.
        Start adding nodes to the head first from the right side and then the left           side alternatively and add the middle node at the end."""
        # 1 2 3 4 5
        # 1 3 2 4 5
        # 1 3 4 2 5
        # 1 3 4 5 2
        # 1 4 3 5 2
        # 1 4 5 3 2
        # 1 4 5 2 3
        # 1 5 4 2 3
        # 1 5 2 4 3
        if head == None:
            return None
        nodes = []
        curr = head
        count = 0
        while curr:
            nodes.append(curr)
            curr = curr.next
            count += 1
        middle = count // 2
        
        for i in range(middle):
            nodes[i].next = nodes[count - i - 1]
            nodes[count - i - 1].next = nodes[i + 1]
        nodes[middle].next = None
        
