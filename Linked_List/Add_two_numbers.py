def addTwoNumbers(self, l1, l2):
        """
        https://leetcode.com/problems/add-two-numbers/
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        curr1 = l1
        curr2 = l2
        carry = 0
        head_curr = head
        while curr1 != None or curr2 != None:
            x = 0
            y = 0
            if curr1 != None:
                x = curr1.val
                curr1 = curr1.next
            if curr2 != None:
                y = curr2.val
                curr2 = curr2.next
            xy_sum = x + y + carry
            carry = int(xy_sum/10)
            head_curr.next = ListNode(xy_sum%10)
            head_curr = head_curr.next
        if carry > 0:
            head_curr.next = ListNode(carry)
        return head.next

#       OR ANOTHER METHOD BUT SLOWER
def addTwoNumbers1(self, l1, l2):
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
        l1_string = ''
        l2_string = ''
        for i in range(max(len(l1_list), len(l2_list))):
            if i < len(l1_list):
                l1_string += str(l1_list[len(l1_list) - i - 1])
            if i < len(l2_list):
                l2_string += str(l2_list[len(l2_list) - i - 1])
        total_string = str(int(l1_string) + int(l2_string))
        
        head = ListNode(int(total_string[len(total_string) - 1]))
        curr = head
        for j in range(len(total_string)-2,-1,-1):
            curr.next = ListNode(int(total_string[j]))
            curr = curr.next
        return head
