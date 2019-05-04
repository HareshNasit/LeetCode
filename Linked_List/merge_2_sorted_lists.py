def mergeTwoLists(self, l1, l2):
        """
        https://leetcode.com/problems/merge-two-sorted-lists/
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #Brute Force, Run Time O((m + n)*log(m+n)) where m and n are the sizes of 
        #the lists.
        all_nodes = []
        curr_l1 = l1
        curr_l2 = l2
        while curr_l1 != None or curr_l2 != None:
            if curr_l1 != None:
                all_nodes.append(curr_l1.val)
                curr_l1 = curr_l1.next
            if curr_l2:
                all_nodes.append(curr_l2.val)
                curr_l2 = curr_l2.next
        print all_nodes
        all_nodes.sort()
        new_list = ListNode(0)
        curr = new_list
        count = 0
        while count < len(all_nodes):
            curr.next = ListNode(all_nodes[count])
            print curr.val
            curr = curr.next
            count += 1
        new_list = new_list.next
        return new_list
                
