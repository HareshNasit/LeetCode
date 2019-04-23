def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        
        """ Divide the problem into 3 cases.
            Case 1:
                If the node to be deleted is a leaf, set it to be None
            Case 2:
                If the node has 1 child, replace the node to be deleted with that 
                only child
            Case 3:
                If the node has both the children, find the successor of the node by
                traversing to the left most node on the right child of the root.
                Replace the nodes value with the successor and since the successor 
                node has atmost 1 child, delete it like case2
        """
