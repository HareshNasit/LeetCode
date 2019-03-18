def isPalindrome(self, head):
        """
        https://leetcode.com/problems/palindrome-linked-list/
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        indexes = {}
        index = 0
        while curr != None:
            indexes[index] = curr.val
            curr = curr.next
            index += 1
        h = indexes.values()
        for i in range(len(h)):
            print(h[i])
            if h[i] != h[len(h) - i - 1]:
                return False
        return True
