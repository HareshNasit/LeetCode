def mergeKLists(self, lists):
        """
        https://leetcode.com/problems/merge-k-sorted-lists/
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        """Consider k min heaps.
        For each index i of all the sorted linked lists, add the elements to 
        all of the heaps in the order of their index.
        
        """
