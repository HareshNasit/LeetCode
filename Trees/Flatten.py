 def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        '''
            Brute Force:
                Traverse all the elements and append them to a list and then make
                a linked list with that.
                
                Traverse the left node, then right node and then the root
                
                '''
