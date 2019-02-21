def inorderTraversal(self, root):
        """
        https://leetcode.com/problems/binary-tree-inorder-traversal/solution/
        :type root: TreeNode
        :rtype: List[int]
        """
       
        if root == None:
            return []
        inorder = []
        if root.left != None:
            inorder += self.inorderTraversal(root.left)
        inorder.append(root.val)
        if root.right != None:
            inorder += self.inorderTraversal(root.right)
        return inorder
