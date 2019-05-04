def middleNode(self, head):
        """
        https://leetcode.com/problems/middle-of-the-linked-list/submissions/
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        nodes_lst = []
        while curr:
            nodes_lst.append(curr)
            curr = curr.next
        if len(nodes_lst) == 0:
            return None
        return nodes_lst[(len(nodes_lst))/ 2]
                #OR
#         curr = head
#         nodes = 0
#         while curr != None:
#             nodes += 1
#             curr = curr.next
#         mid = nodes / 2
#         curr = head
#         count = 0
#         while curr and count < mid:
#             count += 1
#             curr = curr.next
#         return curr
            
