def addTwoNumbers(self, l1, l2):
        """
        https://leetcode.com/problems/add-two-numbers-ii/submissions/
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = []
        l2_list = []
        curr1 = l1
        curr2 = l2
        while curr1 != None or curr2 != None:
            if curr1 != None:
                l1_list.append(curr1.val)
                curr1 = curr1.next
            if curr2 != None:
                l2_list.append(curr2.val)
                curr2 = curr2.next
        l1_string = ''.join(map(str,l1_list))
        l2_string = ''.join(map(str,l2_list))
        l1_int = int(l1_string)
        l2_int = int(l2_string)
        
        sum_l1_l2 = l1_int + l2_int
        string_sum = str(sum_l1_l2)
        
        head = ListNode(string_sum[0])
        curr = head
        for i in range(1,len(string_sum)):
            new_node = ListNode(string_sum[i])
            curr.next = new_node
            curr = curr.next
        return head
