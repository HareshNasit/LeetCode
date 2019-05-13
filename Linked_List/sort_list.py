def sortList(self, head):
        """
        https://leetcode.com/problems/sort-list/
        :type head: ListNode
        :rtype: ListNode
        """
        #Brute Force Time complexity O(nlogn)
        curr = head
        nodes = []
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        nodes.sort()
        curr = head
        index = 0
        while curr:
            curr.val = nodes[index]
            curr = curr.next
            index += 1
        return head
